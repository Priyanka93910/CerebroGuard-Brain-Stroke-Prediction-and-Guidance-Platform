import sqlite3

DB = "cerebroguard.db"   # run this from your project folder

conn = sqlite3.connect(DB)
cursor = conn.cursor()

cursor.execute("SELECT account_id, username, full_name, is_verified FROM doctor_accounts")
rows = cursor.fetchall()

if not rows:
    print("No doctor accounts found.")
else:
    print("Doctor Accounts:")
    for r in rows:
        status = "✅ Verified" if r[3] else "⏳ Pending"
        print(f"  ID={r[0]}  username={r[1]}  name={r[2]}  {status}")

    cursor.execute("UPDATE doctor_accounts SET is_verified=1 WHERE is_verified=0")
    updated = cursor.rowcount
    conn.commit()
    print(f"\nApproved {updated} doctor account(s). All doctors can now login.")

conn.close()