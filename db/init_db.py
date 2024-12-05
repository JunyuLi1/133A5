import sqlite3

db_name = "note.db"
conn = sqlite3.connect(db_name)

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS note (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user INTEGER NOT NULL,
    time TEXT NOT NULL,
    note TEXT NOT NULL,
    weather TEXT NOT NULL
)
""")
conn.commit()

cursor.execute("INSERT INTO note (user, note) VALUES (?, ?)", (1, "TEST1"))
cursor.execute("INSERT INTO note (user, note) VALUES (?, ?)", (2, "TEST2"))
conn.commit()