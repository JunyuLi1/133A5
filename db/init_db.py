import sqlite3

db_name = "note.db"
conn = sqlite3.connect(db_name)

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS note (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    time TEXT NOT NULL,
    note TEXT NOT NULL
)
""")
conn.commit()

cursor.execute("INSERT INTO note (username, time, note) VALUES (?, ?, ?)", ("VC1", "2024-12-5 17:29:21", "TEST1"))
cursor.execute("INSERT INTO note (username, time, note) VALUES (?, ?, ?)", ("VC1", "2024-12-5 17:29:21", "TEST2"))
cursor.execute("INSERT INTO note (username, time, note) VALUES (?, ?, ?)", ("VC1", "2024-12-5 17:29:21", "TEST3"))
cursor.execute("INSERT INTO note (username, time, note) VALUES (?, ?, ?)", ("Hammerbara", "2024-12-5 17:29:21", "TEST4"))
conn.commit()