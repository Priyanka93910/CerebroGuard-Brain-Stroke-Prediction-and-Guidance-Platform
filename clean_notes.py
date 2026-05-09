import sqlite3

DB_NAME = "cerebroguard.db"   # change ONLY if your db name is different

conn = sqlite3.connect(DB_NAME)
cur = conn.cursor()

cur.execute("""
UPDATE predictions
SET notes = NULL
WHERE notes LIKE '%<%';
""")

conn.commit()
conn.close()

print("✅ HTML notes cleaned successfully")
