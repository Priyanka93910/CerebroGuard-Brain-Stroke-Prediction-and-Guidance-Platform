"""
Run this once from your project folder to fix the 'No available slots' issue.
    python fix_slots.py
"""
import sqlite3
import random
from datetime import datetime, timedelta

DB = "cerebroguard.db"

conn = sqlite3.connect(DB)
conn.row_factory = sqlite3.Row
cursor = conn.cursor()

today = datetime.now().strftime("%Y-%m-%d")

# Delete all old expired unbooked slots
cursor.execute("DELETE FROM doctor_availability WHERE date < ? AND is_booked = 0", (today,))
deleted = cursor.rowcount
print(f"🗑️  Removed {deleted} expired slot(s)")

# Get all active doctors
cursor.execute("SELECT doctor_id, name FROM doctors WHERE available = 1")
doctors = cursor.fetchall()
print(f"👨‍⚕️  Found {len(doctors)} doctor(s)")

all_slots = [
    "09:00 AM","09:30 AM","10:00 AM","10:30 AM",
    "11:00 AM","11:30 AM","02:00 PM","02:30 PM",
    "03:00 PM","03:30 PM","04:00 PM","04:30 PM"
]

added = 0
for doc in doctors:
    for offset in range(1, 15):   # next 14 days
        slot_date = (datetime.now() + timedelta(days=offset)).strftime("%Y-%m-%d")

        # Skip if slots already exist for this doctor+date
        cursor.execute("""SELECT COUNT(*) as cnt FROM doctor_availability
            WHERE doctor_id=? AND date=?""", (doc['doctor_id'], slot_date))
        if cursor.fetchone()['cnt'] > 0:
            continue

        for s in random.sample(all_slots, 8):
            cursor.execute("""INSERT INTO doctor_availability
                (doctor_id, date, time_slot, is_booked) VALUES (?,?,?,0)""",
                (doc['doctor_id'], slot_date, s))
            added += 1

conn.commit()
conn.close()

print(f"✅  Added {added} fresh slot(s) for the next 14 days")
print("✅  Done! Restart your Streamlit app and slots will now show correctly.")