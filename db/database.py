import sqlite3


def edit_note(id, username, time, description, category):
    status = False
    conn = sqlite3.connect("note.db")
    c = conn.cursor()
    try:
        c.execute("UPDATE note SET username = ?, time = ?, description = ?, category = ? WHERE id= ?", (username, time, description, category, id))
        conn.commit()
        status = True
    except sqlite3.IntegrityError:
        pass
    finally:
        conn.close()
        return status

def insert_note(username, time, description, category):
    status = False
    conn = sqlite3.connect("note.db")
    c = conn.cursor()
    try:
        c.execute("INSERT INTO note (username, time, description, category) VALUES (?, ?, ?, ?)", (username, time, description, category))
        conn.commit()
        status = True
    except sqlite3.IntegrityError:
        pass
    finally:
        conn.close()
        return status


def load_note(username):
    conn = sqlite3.connect("note.db")
    c = conn.cursor()
    c.execute("SELECT id, time, description, category FROM note WHERE username=?", (username,))
    user_note = c.fetchall()
    conn.close()
    result_note = []
    for item in user_note:
        temp = { 'id': item[0], 'time': item[1], 'description': item[2], 'category': item[3] }
        result_note.append(temp)
    return result_note

def request_user(username, password):
    conn = sqlite3.connect("user.db")
    c = conn.cursor()
    c.execute("SELECT id FROM user WHERE username=? AND password=?", (username, password))
    user = c.fetchone()
    conn.close()
    if user:
        return True
    else:
        return False


def register_user(username, password):
    # regist user
    status = False
    conn = sqlite3.connect("user.db")
    c = conn.cursor()
    try:
        c.execute("INSERT INTO user (username, password) VALUES (?, ?)", (username, password))
        conn.commit()
        print("User registered successfully!")
        status = True
    except sqlite3.IntegrityError:
        print("User already exists!")
    finally:
        conn.close()
        return status

if __name__ == "__main__":
    print(load_note("VC1"))