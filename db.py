import sqlite3

def create_db():
    conn = sqlite3.connect("repo.db")
    conn.execute("create table data (id INTEGER primary key, label text, link text, type text)")
    conn.commit()

def connect():
    conn = sqlite3.connect("repo.db")
    conn.row_factory = sqlite3.Row
    return conn

if __name__ == '__main__':
    create_db()
