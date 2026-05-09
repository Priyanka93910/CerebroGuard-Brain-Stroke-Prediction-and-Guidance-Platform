import sqlite3
import hashlib
from datetime import datetime, timedelta
from contextlib import contextmanager

DATABASE_NAME = "cerebroguard.db"

# ══════════════════════════════════════════════════════════════
# CONNECTION
# ══════════════════════════════════════════════════════════════
@contextmanager
def get_db_connection():
    conn = sqlite3.connect(DATABASE_NAME)
    conn.row_factory = sqlite3.Row
    try:
        yield conn
        conn.commit()
    except Exception as e:
        conn.rollback()
        raise e
    finally:
        conn.close()

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


# ══════════════════════════════════════════════════════════════
# DATABASE INITIALIZATION
# NOTE: Uses CREATE TABLE IF NOT EXISTS — NEVER drops tables.
#       Safe to call on every app startup.
# ══════════════════════════════════════════════════════════════
def init_database():
    with get_db_connection() as conn:
        cursor = conn.cursor()

        # ── 1. USERS (patients) ───────────────────────────────
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            user_id       INTEGER PRIMARY KEY AUTOINCREMENT,
            username      TEXT UNIQUE NOT NULL,
            email         TEXT UNIQUE NOT NULL,
            password_hash TEXT NOT NULL,
            full_name     TEXT,
            phone         TEXT,
            date_of_birth TEXT,
            gender        TEXT CHECK(gender IN ('Male','Female','Other','Prefer not to say')),
            created_at    TEXT DEFAULT CURRENT_TIMESTAMP,
            last_login    TEXT,
            is_active     INTEGER DEFAULT 1
        )""")

        # ── 2. PREDICTIONS ────────────────────────────────────
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS predictions (
            prediction_id    INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id          INTEGER REFERENCES users(user_id) ON DELETE CASCADE,
            age              INTEGER NOT NULL,
            gender           TEXT,
            hypertension     INTEGER,
            heart_disease    INTEGER,
            ever_married     INTEGER,
            work_type        TEXT,
            residence_type   TEXT,
            bmi              REAL,
            glucose_level    REAL,
            smoking_status   TEXT,
            risk_probability REAL CHECK(risk_probability BETWEEN 0 AND 1),
            risk_level       TEXT CHECK(risk_level IN ('High','Low')),
            model_used       TEXT DEFAULT 'Random Forest',
            prediction_date  TEXT DEFAULT CURRENT_TIMESTAMP,
            notes            TEXT
        )""")

        # ── 3. DOCTOR CATALOGUE (seeded, patient-facing) ──────
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS doctors (
            doctor_id        INTEGER PRIMARY KEY AUTOINCREMENT,
            name             TEXT NOT NULL,
            specialty        TEXT,
            hospital         TEXT,
            address          TEXT,
            city             TEXT,
            phone            TEXT,
            email            TEXT,
            experience_years INTEGER,
            rating           REAL DEFAULT 4.0,
            latitude         REAL,
            longitude        REAL,
            consultation_fee INTEGER DEFAULT 500,
            languages        TEXT DEFAULT 'English, Telugu, Hindi',
            bio              TEXT,
            available        INTEGER DEFAULT 1
        )""")

        # ── 4. DOCTOR ACCOUNTS (login portal) ─────────────────
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS doctor_accounts (
            account_id       INTEGER PRIMARY KEY AUTOINCREMENT,
            username         TEXT UNIQUE NOT NULL,
            email            TEXT UNIQUE NOT NULL,
            password_hash    TEXT NOT NULL,
            full_name        TEXT NOT NULL,
            specialty        TEXT,
            hospital         TEXT,
            license_number   TEXT UNIQUE NOT NULL,
            phone            TEXT,
            experience_years INTEGER DEFAULT 0,
            is_verified      INTEGER DEFAULT 1,
            is_active        INTEGER DEFAULT 1,
            created_at       TEXT DEFAULT CURRENT_TIMESTAMP,
            last_login       TEXT
        )""")

        # ── 5. AVAILABILITY SLOTS ─────────────────────────────
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS doctor_availability (
            slot_id        INTEGER PRIMARY KEY AUTOINCREMENT,
            doctor_id      INTEGER REFERENCES doctors(doctor_id) ON DELETE CASCADE,
            date           TEXT NOT NULL,
            time_slot      TEXT NOT NULL,
            is_booked      INTEGER DEFAULT 0,
            booked_by_user INTEGER REFERENCES users(user_id),
            booked_at      TEXT
        )""")

        # ── 6. SLOT-BASED APPOINTMENTS ────────────────────────
        #    (used when booking from the doctor catalogue)
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS appointments (
            appointment_id   INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id          INTEGER REFERENCES users(user_id) ON DELETE CASCADE,
            doctor_id        INTEGER REFERENCES doctors(doctor_id),
            slot_id          INTEGER REFERENCES doctor_availability(slot_id),
            prediction_id    INTEGER REFERENCES predictions(prediction_id),
            status           TEXT DEFAULT 'Confirmed',
            booked_at        TEXT DEFAULT CURRENT_TIMESTAMP,
            patient_notes    TEXT,
            doctor_name      TEXT,
            hospital_name    TEXT,
            appointment_date TEXT,
            appointment_time TEXT
        )""")

        # ── 7. CONSULTATION NOTES ─────────────────────────────
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS consultation_notes (
            note_id           INTEGER PRIMARY KEY AUTOINCREMENT,
            appointment_id    INTEGER REFERENCES appointments(appointment_id) ON DELETE CASCADE,
            doctor_account_id INTEGER REFERENCES doctor_accounts(account_id),
            patient_user_id   INTEGER REFERENCES users(user_id),
            diagnosis         TEXT,
            prescription      TEXT,
            recommendations   TEXT,
            follow_up_date    TEXT,
            created_at        TEXT DEFAULT CURRENT_TIMESTAMP,
            updated_at        TEXT DEFAULT CURRENT_TIMESTAMP
        )""")

        # ── 8. WALK-IN APPOINTMENTS ───────────────────────────
        #    (used by DoctorFinder page — real hospitals from OSM)
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS walk_in_appointments (
            walkin_id     INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id       INTEGER NOT NULL,
            username      TEXT NOT NULL,
            hospital_name TEXT NOT NULL,
            hospital_addr TEXT,
            hospital_lat  REAL,
            hospital_lon  REAL,
            appt_date     TEXT NOT NULL,
            appt_time     TEXT NOT NULL,
            reason        TEXT,
            status        TEXT DEFAULT 'Confirmed',
            booked_at     TEXT DEFAULT CURRENT_TIMESTAMP
        )""")

        # Indexes
        cursor.execute("CREATE INDEX IF NOT EXISTS idx_pred_user   ON predictions(user_id)")
        cursor.execute("CREATE INDEX IF NOT EXISTS idx_pred_date   ON predictions(prediction_date)")
        cursor.execute("CREATE INDEX IF NOT EXISTS idx_appt_user   ON appointments(user_id)")
        cursor.execute("CREATE INDEX IF NOT EXISTS idx_appt_doc    ON appointments(doctor_id)")
        cursor.execute("CREATE INDEX IF NOT EXISTS idx_slots_doc   ON doctor_availability(doctor_id)")
        cursor.execute("CREATE INDEX IF NOT EXISTS idx_notes_appt  ON consultation_notes(appointment_id)")
        cursor.execute("CREATE INDEX IF NOT EXISTS idx_walkin_user ON walk_in_appointments(user_id)")

        # Seed doctors and refresh slots
        _seed_doctors_if_empty(cursor)
        print("Database initialized successfully!")


# ══════════════════════════════════════════════════════════════
# SEED HYDERABAD NEUROLOGISTS
# ══════════════════════════════════════════════════════════════
def _seed_doctors_if_empty(cursor):
    cursor.execute("SELECT COUNT(*) as cnt FROM doctors")
    if cursor.fetchone()['cnt'] > 0:
        _refresh_slots_if_expired(cursor)
        return

    rows = [
        ("Dr. Sudhir Kumar","Neurologist & Stroke Specialist","Apollo Hospitals",
         "Jubilee Hills, Road No. 72","Hyderabad","+91-40-2360-7777",
         "sudhir.kumar@apollohyd.com",18,4.8,17.4239,78.4483,800,"English, Telugu, Hindi",
         "Senior neurologist specializing in stroke management, epilepsy, and movement disorders."),
        ("Dr. Rupam Borgohain","Senior Neurologist","Yashoda Hospitals",
         "Raj Bhavan Road, Somajiguda","Hyderabad","+91-40-4567-4567",
         "borgohain@yashodahyd.com",22,4.9,17.4196,78.4601,1000,"English, Hindi, Assamese",
         "Head of Neurosciences at Yashoda. Expert in Parkinson's, stroke, neuro-critical care."),
        ("Dr. Anitha Rudraiah","Interventional Neurologist","KIMS Hospital",
         "Minister Road, Secunderabad","Hyderabad","+91-40-4488-5000",
         "anitha.r@kimshyd.com",14,4.7,17.4399,78.4983,700,"English, Telugu, Kannada",
         "Specialist in interventional neurology and acute stroke treatment."),
        ("Dr. Praveen Kumar Nalla","Neuro-Physician","Care Hospitals",
         "Exhibition Road, Nampally","Hyderabad","+91-40-3041-8888",
         "praveen.n@carehyd.com",12,4.6,17.3850,78.4867,600,"English, Telugu, Hindi",
         "Experienced in hypertensive stroke, diabetic neuropathy, cerebrovascular diseases."),
        ("Dr. Padma Srivastava","Neurologist","NIMS",
         "Punjagutta, NIMS Road","Hyderabad","+91-40-2348-9000",
         "padma.s@nims.edu.in",25,4.9,17.4255,78.4483,400,"English, Hindi, Telugu",
         "Renowned neurologist and researcher. Head of Dept at NIMS."),
        ("Dr. Virender Sachdeva","Cerebrovascular Surgeon","Continental Hospitals",
         "IT Park Road, Nanakramguda","Hyderabad","+91-40-6700-0000",
         "sachdeva@continentalhyd.com",16,4.7,17.4075,78.3490,900,"English, Hindi, Punjabi",
         "Cerebrovascular and endovascular neurosurgeon specializing in aneurysm treatment."),
        ("Dr. Meena Gupta","Stroke & Rehabilitation Specialist","Medicover Hospitals",
         "Madhapur, Hi-Tech City","Hyderabad","+91-40-6801-6801",
         "meena.g@medicoverhyd.com",10,4.5,17.4486,78.3908,650,"English, Hindi, Telugu",
         "Focuses on acute stroke management and post-stroke rehabilitation."),
        ("Dr. Ravi Shankar Reddy","Neurologist","Sunshine Hospitals",
         "Penderghast Road, Secunderabad","Hyderabad","+91-40-4444-4444",
         "ravi.reddy@sunshinehyd.com",13,4.6,17.4503,78.5015,550,"English, Telugu, Hindi",
         "Expert in epilepsy, stroke, and headache management."),
    ]
    for r in rows:
        cursor.execute("""INSERT INTO doctors
            (name,specialty,hospital,address,city,phone,email,
             experience_years,rating,latitude,longitude,consultation_fee,languages,bio)
            VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?)""", r)

    cursor.execute("SELECT doctor_id FROM doctors")
    doc_ids = [row['doctor_id'] for row in cursor.fetchall()]
    _generate_slots_for_doctors(cursor, doc_ids, days=14)


def _refresh_slots_if_expired(cursor):
    today = datetime.now().strftime("%Y-%m-%d")
    cursor.execute("""SELECT COUNT(*) as cnt FROM doctor_availability
        WHERE date >= ? AND is_booked = 0""", (today,))
    if cursor.fetchone()['cnt'] < 10:
        cursor.execute("DELETE FROM doctor_availability WHERE date < ? AND is_booked = 0",
                       (today,))
        cursor.execute("SELECT doctor_id FROM doctors WHERE available = 1")
        doc_ids = [row['doctor_id'] for row in cursor.fetchall()]
        _generate_slots_for_doctors(cursor, doc_ids, days=14)


def _generate_slots_for_doctors(cursor, doc_ids, days=14):
    import random
    all_slots = ["09:00 AM","09:30 AM","10:00 AM","10:30 AM",
                 "11:00 AM","11:30 AM","02:00 PM","02:30 PM",
                 "03:00 PM","03:30 PM","04:00 PM","04:30 PM"]
    today = datetime.now()
    for doc_id in doc_ids:
        for offset in range(1, days + 1):
            slot_date = (today + timedelta(days=offset)).strftime("%Y-%m-%d")
            cursor.execute("""SELECT COUNT(*) as cnt FROM doctor_availability
                WHERE doctor_id=? AND date=?""", (doc_id, slot_date))
            if cursor.fetchone()['cnt'] > 0:
                continue
            for s in random.sample(all_slots, 8):
                cursor.execute("""INSERT INTO doctor_availability
                    (doctor_id,date,time_slot,is_booked) VALUES (?,?,?,0)""",
                    (doc_id, slot_date, s))


# ══════════════════════════════════════════════════════════════
# USER (PATIENT) CRUD
# ══════════════════════════════════════════════════════════════
def create_user(username, email, password, full_name=None,
                phone=None, date_of_birth=None, gender=None):
    with get_db_connection() as conn:
        cursor = conn.cursor()
        try:
            cursor.execute("""INSERT INTO users
                (username,email,password_hash,full_name,phone,date_of_birth,gender)
                VALUES (?,?,?,?,?,?,?)""",
                (username, email, hash_password(password),
                 full_name, phone, date_of_birth, gender))
            user_id = cursor.lastrowid
            print(f"User created: {username} (ID: {user_id})")
            return user_id
        except sqlite3.IntegrityError:
            print(f"User already exists: {username}")
            return None

def authenticate_user(username, password):
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("""SELECT user_id,username,email,full_name,is_active
            FROM users WHERE username=? AND password_hash=? AND is_active=1""",
            (username, hash_password(password)))
        user = cursor.fetchone()
        if user:
            cursor.execute("UPDATE users SET last_login=? WHERE user_id=?",
                           (datetime.now().isoformat(), user['user_id']))
            return dict(user)
        return None

def get_user(user_id):
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE user_id=?", (user_id,))
        r = cursor.fetchone()
        return dict(r) if r else None

def update_user_email(user_id, new_email):
    with get_db_connection() as conn:
        cursor = conn.cursor()
        try:
            cursor.execute("UPDATE users SET email=? WHERE user_id=?", (new_email, user_id))
            return cursor.rowcount > 0
        except sqlite3.IntegrityError:
            return False

def update_user_profile(user_id, full_name=None, phone=None,
                        date_of_birth=None, gender=None):
    with get_db_connection() as conn:
        cursor = conn.cursor()
        updates, params = [], []
        if full_name     is not None: updates.append("full_name=?");     params.append(full_name)
        if phone         is not None: updates.append("phone=?");         params.append(phone)
        if date_of_birth is not None: updates.append("date_of_birth=?"); params.append(date_of_birth)
        if gender        is not None: updates.append("gender=?");        params.append(gender)
        if not updates: return False
        params.append(user_id)
        cursor.execute(f"UPDATE users SET {','.join(updates)} WHERE user_id=?", params)
        return cursor.rowcount > 0

def delete_user(user_id):
    with get_db_connection() as conn:
        cursor = conn.cursor()
        try:
            cursor.execute("DELETE FROM predictions WHERE user_id=?", (user_id,))
            cursor.execute("DELETE FROM users WHERE user_id=?", (user_id,))
            return cursor.rowcount > 0
        except Exception as e:
            print(f"Delete failed: {e}")
            return False

def get_all_patients():
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("""SELECT user_id,username,full_name,email,phone,
            date_of_birth,gender,created_at,last_login
            FROM users WHERE is_active=1 ORDER BY full_name""")
        return [dict(r) for r in cursor.fetchall()]


# ══════════════════════════════════════════════════════════════
# DOCTOR ACCOUNT CRUD
# ══════════════════════════════════════════════════════════════
def create_doctor_account(username, email, password, full_name, specialty,
                          hospital, license_number, phone=None, experience_years=0):
    """Register a doctor — auto-verified for immediate login."""
    with get_db_connection() as conn:
        cursor = conn.cursor()
        try:
            cursor.execute("""INSERT INTO doctor_accounts
                (username,email,password_hash,full_name,specialty,hospital,
                 license_number,phone,experience_years,is_verified)
                VALUES (?,?,?,?,?,?,?,?,?,1)""",
                (username, email, hash_password(password), full_name,
                 specialty, hospital, license_number, phone, experience_years))
            return cursor.lastrowid
        except sqlite3.IntegrityError:
            return None

def authenticate_doctor(username, password):
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("""SELECT * FROM doctor_accounts
            WHERE username=? AND password_hash=? AND is_active=1""",
            (username, hash_password(password)))
        doc = cursor.fetchone()
        if doc:
            cursor.execute("UPDATE doctor_accounts SET last_login=? WHERE account_id=?",
                           (datetime.now().isoformat(), doc['account_id']))
            return dict(doc)
        return None

def get_doctor_account(account_id):
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM doctor_accounts WHERE account_id=?", (account_id,))
        r = cursor.fetchone()
        return dict(r) if r else None

def get_all_doctor_accounts():
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("""SELECT account_id,username,full_name,specialty,
            hospital,license_number,is_verified,created_at
            FROM doctor_accounts ORDER BY created_at DESC""")
        return [dict(r) for r in cursor.fetchall()]

def verify_doctor_account(account_id):
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("UPDATE doctor_accounts SET is_verified=1 WHERE account_id=?",
                       (account_id,))
        return cursor.rowcount > 0

def update_doctor_profile(account_id, full_name=None, specialty=None,
                          hospital=None, phone=None, experience_years=None):
    with get_db_connection() as conn:
        cursor = conn.cursor()
        updates, params = [], []
        if full_name        is not None: updates.append("full_name=?");        params.append(full_name)
        if specialty        is not None: updates.append("specialty=?");        params.append(specialty)
        if hospital         is not None: updates.append("hospital=?");         params.append(hospital)
        if phone            is not None: updates.append("phone=?");            params.append(phone)
        if experience_years is not None: updates.append("experience_years=?"); params.append(experience_years)
        if not updates: return False
        params.append(account_id)
        cursor.execute(f"UPDATE doctor_accounts SET {','.join(updates)} WHERE account_id=?", params)
        return cursor.rowcount > 0


# ══════════════════════════════════════════════════════════════
# PREDICTION CRUD
# ══════════════════════════════════════════════════════════════
def save_prediction(user_id, age, gender, bmi, glucose_level,
                    risk_probability, risk_level,
                    hypertension=0, heart_disease=0, ever_married=0,
                    work_type=None, residence_type=None, smoking_status=None,
                    notes=None, model_used='Random Forest'):
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("""INSERT INTO predictions
            (user_id,age,gender,hypertension,heart_disease,ever_married,
             work_type,residence_type,bmi,glucose_level,smoking_status,
             risk_probability,risk_level,model_used,notes)
            VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""",
            (user_id, age, gender, hypertension, heart_disease, ever_married,
             work_type, residence_type, bmi, glucose_level, smoking_status,
             risk_probability, risk_level, model_used, notes))
        pred_id = cursor.lastrowid
        print(f"Prediction saved (ID: {pred_id}) for user {user_id}")
        return pred_id

def get_user_predictions(user_id, limit=20):
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("""SELECT * FROM predictions WHERE user_id=?
            ORDER BY prediction_date DESC LIMIT ?""", (user_id, limit))
        return [dict(r) for r in cursor.fetchall()]

def get_prediction(prediction_id):
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM predictions WHERE prediction_id=?", (prediction_id,))
        r = cursor.fetchone()
        return dict(r) if r else None

def get_prediction_statistics(user_id):
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("""SELECT COUNT(*) as total_predictions,
            AVG(risk_probability) as avg_risk,
            MAX(risk_probability) as max_risk,
            MIN(risk_probability) as min_risk,
            SUM(CASE WHEN risk_level='High' THEN 1 ELSE 0 END) as high_risk_count,
            SUM(CASE WHEN risk_level='Low'  THEN 1 ELSE 0 END) as low_risk_count
            FROM predictions WHERE user_id=?""", (user_id,))
        return dict(cursor.fetchone())

def get_patient_predictions_for_doctor(user_id):
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("""SELECT p.*, u.full_name, u.email, u.phone
            FROM predictions p JOIN users u ON p.user_id=u.user_id
            WHERE p.user_id=? ORDER BY p.prediction_date DESC""", (user_id,))
        return [dict(r) for r in cursor.fetchall()]

def get_all_high_risk_patients():
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("""SELECT u.user_id, u.full_name, u.email, u.phone,
            COUNT(p.prediction_id) as total_checks,
            MAX(p.risk_probability) as max_risk,
            MAX(p.prediction_date) as last_check
            FROM users u JOIN predictions p ON u.user_id=p.user_id
            WHERE p.risk_level='High'
            GROUP BY u.user_id ORDER BY max_risk DESC""")
        return [dict(r) for r in cursor.fetchall()]

def update_prediction_notes(prediction_id, notes):
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("UPDATE predictions SET notes=? WHERE prediction_id=?",
                       (notes, prediction_id))
        return cursor.rowcount > 0

def delete_prediction(prediction_id):
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM predictions WHERE prediction_id=?", (prediction_id,))
        return cursor.rowcount > 0

def delete_all_user_predictions(user_id):
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM predictions WHERE user_id=?", (user_id,))
        return cursor.rowcount


# ══════════════════════════════════════════════════════════════
# DOCTOR CATALOGUE
# ══════════════════════════════════════════════════════════════
def get_all_doctors():
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM doctors WHERE available=1 ORDER BY rating DESC")
        return [dict(r) for r in cursor.fetchall()]

def get_doctors_near(lat, lon, radius_km=15):
    import math
    results = []
    for doc in get_all_doctors():
        dist = math.sqrt((doc['latitude']-lat)**2 + (doc['longitude']-lon)**2) * 111
        if dist <= radius_km:
            doc['distance_km'] = round(dist, 1)
            results.append(doc)
    results.sort(key=lambda x: x['distance_km'])
    return results

def get_doctor_available_slots(doctor_id, date=None):
    with get_db_connection() as conn:
        cursor = conn.cursor()
        if date:
            cursor.execute("""SELECT * FROM doctor_availability
                WHERE doctor_id=? AND date=? AND is_booked=0 ORDER BY time_slot""",
                (doctor_id, date))
        else:
            cursor.execute("""SELECT * FROM doctor_availability
                WHERE doctor_id=? AND is_booked=0 AND date>=date('now')
                ORDER BY date,time_slot""", (doctor_id,))
        return [dict(r) for r in cursor.fetchall()]

def get_available_dates_for_doctor(doctor_id):
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("""SELECT DISTINCT date FROM doctor_availability
            WHERE doctor_id=? AND is_booked=0 AND date>=date('now') ORDER BY date""",
            (doctor_id,))
        return [r['date'] for r in cursor.fetchall()]


# ══════════════════════════════════════════════════════════════
# SLOT-BASED APPOINTMENTS (doctor catalogue booking)
# ══════════════════════════════════════════════════════════════
def book_appointment(user_id, doctor_id, slot_id, patient_notes=None, prediction_id=None):
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(
            "SELECT * FROM doctor_availability WHERE slot_id=? AND is_booked=0", (slot_id,))
        slot = cursor.fetchone()
        if not slot: return None
        cursor.execute("SELECT name,hospital FROM doctors WHERE doctor_id=?", (doctor_id,))
        doc = cursor.fetchone()
        cursor.execute("""UPDATE doctor_availability
            SET is_booked=1,booked_by_user=?,booked_at=? WHERE slot_id=?""",
            (user_id, datetime.now().isoformat(), slot_id))
        cursor.execute("""INSERT INTO appointments
            (user_id,doctor_id,slot_id,prediction_id,status,patient_notes,
             doctor_name,hospital_name,appointment_date,appointment_time)
            VALUES (?,?,?,?,'Confirmed',?,?,?,?,?)""",
            (user_id, doctor_id, slot_id, prediction_id, patient_notes,
             doc['name'], doc['hospital'], slot['date'], slot['time_slot']))
        return cursor.lastrowid

def get_user_appointments(user_id):
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("""SELECT a.*, d.phone as doctor_phone,
            d.address as doctor_address, d.specialty as doctor_specialty
            FROM appointments a JOIN doctors d ON a.doctor_id=d.doctor_id
            WHERE a.user_id=? ORDER BY a.appointment_date DESC,a.appointment_time ASC""",
            (user_id,))
        return [dict(r) for r in cursor.fetchall()]

def get_doctor_appointments(doctor_catalogue_id):
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("""SELECT a.*,
            u.full_name as patient_name, u.email as patient_email,
            u.phone as patient_phone, u.date_of_birth, u.gender as patient_gender,
            p.risk_probability, p.risk_level, p.bmi, p.glucose_level,
            p.hypertension, p.heart_disease, p.smoking_status, p.age as patient_age
            FROM appointments a
            JOIN users u ON a.user_id=u.user_id
            LEFT JOIN predictions p ON a.prediction_id=p.prediction_id
            WHERE a.doctor_id=?
            ORDER BY a.appointment_date DESC,a.appointment_time ASC""",
            (doctor_catalogue_id,))
        return [dict(r) for r in cursor.fetchall()]

def cancel_appointment(appointment_id, user_id):
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("""SELECT slot_id FROM appointments
            WHERE appointment_id=? AND user_id=?""", (appointment_id, user_id))
        appt = cursor.fetchone()
        if not appt: return False
        cursor.execute("""UPDATE doctor_availability
            SET is_booked=0,booked_by_user=NULL,booked_at=NULL WHERE slot_id=?""",
            (appt['slot_id'],))
        cursor.execute("UPDATE appointments SET status='Cancelled' WHERE appointment_id=?",
                       (appointment_id,))
        return True


# ══════════════════════════════════════════════════════════════
# WALK-IN APPOINTMENTS (DoctorFinder — real OSM hospitals)
# ══════════════════════════════════════════════════════════════
def book_walkin(user_id, username, hosp_name, hosp_addr,
                h_lat, h_lon, appt_date, appt_time, reason):
    with get_db_connection() as conn:
        conn.execute("""INSERT INTO walk_in_appointments
            (user_id,username,hospital_name,hospital_addr,
             hospital_lat,hospital_lon,appt_date,appt_time,reason)
            VALUES (?,?,?,?,?,?,?,?,?)""",
            (user_id, username, hosp_name, hosp_addr,
             h_lat, h_lon, str(appt_date), appt_time, reason))

def get_walkin_appointments(user_id):
    with get_db_connection() as conn:
        rows = conn.execute("""SELECT * FROM walk_in_appointments
            WHERE user_id=? ORDER BY appt_date DESC,appt_time DESC""",
            (user_id,)).fetchall()
        return [dict(r) for r in rows]

def cancel_walkin(walkin_id):
    with get_db_connection() as conn:
        conn.execute(
            "UPDATE walk_in_appointments SET status='Cancelled' WHERE walkin_id=?",
            (walkin_id,))


# ══════════════════════════════════════════════════════════════
# CONSULTATION NOTES
# ══════════════════════════════════════════════════════════════
def save_consultation_note(appointment_id, doctor_account_id, patient_user_id,
                           diagnosis, prescription, recommendations, follow_up_date=None):
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(
            "SELECT note_id FROM consultation_notes WHERE appointment_id=?",
            (appointment_id,))
        existing = cursor.fetchone()
        now = datetime.now().isoformat()
        if existing:
            cursor.execute("""UPDATE consultation_notes
                SET diagnosis=?,prescription=?,recommendations=?,
                    follow_up_date=?,updated_at=? WHERE note_id=?""",
                (diagnosis, prescription, recommendations,
                 follow_up_date, now, existing['note_id']))
            return existing['note_id']
        else:
            cursor.execute("""INSERT INTO consultation_notes
                (appointment_id,doctor_account_id,patient_user_id,
                 diagnosis,prescription,recommendations,follow_up_date,
                 created_at,updated_at)
                VALUES (?,?,?,?,?,?,?,?,?)""",
                (appointment_id, doctor_account_id, patient_user_id,
                 diagnosis, prescription, recommendations, follow_up_date, now, now))
            return cursor.lastrowid

def get_consultation_note(appointment_id):
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("""SELECT cn.*, da.full_name as doctor_name, da.specialty
            FROM consultation_notes cn
            JOIN doctor_accounts da ON cn.doctor_account_id=da.account_id
            WHERE cn.appointment_id=?""", (appointment_id,))
        r = cursor.fetchone()
        return dict(r) if r else None

def get_patient_notes_for_doctor(doctor_account_id, patient_user_id):
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("""SELECT cn.*, a.appointment_date, a.appointment_time
            FROM consultation_notes cn
            JOIN appointments a ON cn.appointment_id=a.appointment_id
            WHERE cn.doctor_account_id=? AND cn.patient_user_id=?
            ORDER BY cn.created_at DESC""", (doctor_account_id, patient_user_id))
        return [dict(r) for r in cursor.fetchall()]

def get_patient_notes_for_user(patient_user_id):
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("""SELECT cn.*, da.full_name as doctor_name, da.specialty,
            da.hospital, a.appointment_date, a.appointment_time
            FROM consultation_notes cn
            JOIN doctor_accounts da ON cn.doctor_account_id=da.account_id
            JOIN appointments a ON cn.appointment_id=a.appointment_id
            WHERE cn.patient_user_id=? ORDER BY cn.created_at DESC""",
            (patient_user_id,))
        return [dict(r) for r in cursor.fetchall()]


# ══════════════════════════════════════════════════════════════
# AVAILABILITY MANAGEMENT (doctor portal)
# ══════════════════════════════════════════════════════════════
def add_availability_slot(doctor_id, date, time_slot):
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("""SELECT slot_id FROM doctor_availability
            WHERE doctor_id=? AND date=? AND time_slot=?""", (doctor_id, date, time_slot))
        if cursor.fetchone(): return None
        cursor.execute("""INSERT INTO doctor_availability
            (doctor_id,date,time_slot,is_booked) VALUES (?,?,?,0)""",
            (doctor_id, date, time_slot))
        return cursor.lastrowid

def remove_availability_slot(slot_id, doctor_id):
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("""SELECT * FROM doctor_availability
            WHERE slot_id=? AND doctor_id=? AND is_booked=0""", (slot_id, doctor_id))
        if not cursor.fetchone(): return False
        cursor.execute("DELETE FROM doctor_availability WHERE slot_id=?", (slot_id,))
        return cursor.rowcount > 0

def get_all_slots_for_doctor(doctor_id):
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("""SELECT da.*, u.full_name as patient_name, u.phone as patient_phone
            FROM doctor_availability da
            LEFT JOIN users u ON da.booked_by_user=u.user_id
            WHERE da.doctor_id=? AND da.date>=date('now')
            ORDER BY da.date,da.time_slot""", (doctor_id,))
        return [dict(r) for r in cursor.fetchall()]


# ══════════════════════════════════════════════════════════════
# STATS
# ══════════════════════════════════════════════════════════════
def get_database_stats():
    with get_db_connection() as conn:
        cursor = conn.cursor()
        s = {}
        for key, sql in [
            ('total_users',         "SELECT COUNT(*) FROM users"),
            ('total_doctors',       "SELECT COUNT(*) FROM doctors"),
            ('doctor_accounts',     "SELECT COUNT(*) FROM doctor_accounts"),
            ('total_predictions',   "SELECT COUNT(*) FROM predictions"),
            ('total_appointments',  "SELECT COUNT(*) FROM appointments"),
            ('walkin_appointments', "SELECT COUNT(*) FROM walk_in_appointments"),
            ('high_risk_patients',
             "SELECT COUNT(DISTINCT user_id) FROM predictions WHERE risk_level='High'"),
        ]:
            cursor.execute(sql)
            s[key] = cursor.fetchone()[0]
        return s

def clear_all_data():
    """WARNING: Deletes all user data (keeps table structure)."""
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM predictions")
        cursor.execute("DELETE FROM users")
        print("All data cleared!")

def seed_sample_data():
    """Add sample data for testing."""
    u1 = create_user('john_doe','john@example.com','password123',
                     'John Doe','+91-9876543210','1985-05-15','Male')
    u2 = create_user('jane_smith','jane@example.com','password123',
                     'Jane Smith','+91-9876543211','1990-08-22','Female')
    if u1:
        save_prediction(u1,67,'Male',36.6,228.69,0.78,'High',
                        hypertension=1,heart_disease=1,notes='High risk detected')
        save_prediction(u1,67,'Male',35.2,220.0,0.72,'High',
                        hypertension=1,heart_disease=1,notes='Follow-up — still high risk')
    if u2:
        save_prediction(u2,32,'Female',23.5,95.0,0.12,'Low',notes='Healthy — low risk')
    print("Sample data seeded!")


# ══════════════════════════════════════════════════════════════
# MAIN
# ══════════════════════════════════════════════════════════════
if __name__ == "__main__":
    print("Initializing CerebroGuard Database...")
    init_database()
    print("\nDatabase Statistics:")
    for k, v in get_database_stats().items():
        print(f"   {k}: {v}")
    print("\nDone!")
    print("Test credentials: username=john_doe  password=password123")