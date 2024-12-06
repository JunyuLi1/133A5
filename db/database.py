import sqlite3


def insert_note():
    conn = sqlite3.connect("note.db")
    c = conn.cursor
    pass


def load_note():
    pass

def request_user(username, password):
    conn = sqlite3.connect("user.db")
    c = conn.cursor()
    c.execute("SELECT id FROM users WHERE username=? AND password=?", (username, password))
    user = c.fetchone()
    conn.close()
    if user:
        return True
    else:
        return False


def register_user(username, password):
    # regist user
    conn = sqlite3.connect("user.db")
    c = conn.cursor()
    try:
        c.execute("INSERT INTO user (username, password) VALUES (?, ?)", (username, password))
        conn.commit()
        print("User registered successfully!")
    except sqlite3.IntegrityError:
        print("User already exists!")
    finally:
        conn.close()