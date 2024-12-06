import sqlite3

db_name = "note.db"
conn = sqlite3.connect(db_name)

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS note (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    time TEXT NOT NULL,
    description TEXT NOT NULL,
    category TEXT NOT NULL
)
""")
conn.commit()

cursor.execute("INSERT INTO note (username, time, description, category) VALUES (?, ?, ?, ?)", ("VC1", "2024-12-5 17:29:21", "TEST1","a"))
cursor.execute("INSERT INTO note (username, time, description, category) VALUES (?, ?, ?, ?)", ("VC1", "2024-12-5 17:29:21", "TEST2","b"))
cursor.execute("INSERT INTO note (username, time, description, category) VALUES (?, ?, ?, ?)", ("VC1", "2024-12-5 17:29:21", "TEST3","c"))
cursor.execute("INSERT INTO note (username, time, description, category) VALUES (?, ?, ?, ?)", ("Hammerbara", "2024-12-5 17:29:21", "TEST4","a"))
conn.commit()