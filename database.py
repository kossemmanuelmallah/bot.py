import sqlite3

def init_db():
    conn = sqlite3.connect("clients.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS requests (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            message TEXT
        )
    """)
    conn.commit()
    conn.close()

def save_request(user_id, message):
    conn = sqlite3.connect("clients.db")
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO requests (user_id, message) VALUES (?, ?)",
        (user_id, message)
    )
    conn.commit()
    conn.close()
