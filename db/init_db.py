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

cursor.execute("INSERT INTO note (user, time, note, weather) VALUES (?, ?, ?, ?)", (1, "2024-12-5 17:29:21", "TEST1", "Cloudy"))
cursor.execute("INSERT INTO note (user, time, note, weather) VALUES (?, ?, ?, ?)", (2, "2024-12-5 17:29:21", "TEST2", "Cloudy"))
conn.commit()