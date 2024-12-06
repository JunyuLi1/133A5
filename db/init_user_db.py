import sqlite3

db_name = "user.db"
conn = sqlite3.connect(db_name)

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS user (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL
)
""")
conn.commit()

cursor.execute("INSERT INTO user (username, password) VALUES (?, ?)", ("VC1", "123"))
cursor.execute("INSERT INTO user (username, password) VALUES (?, ?)", ("Hammerbara", "123"))
conn.commit()