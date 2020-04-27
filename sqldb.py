import sqlite3
__connection = None


def get_connection() :
    global __connection
    if __connection is None :
        __connection = sqlite3.connect('icq.db')
    return __connection


def init_db() :
    conn = get_connection()
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS users (userId int, nick text, firstName text, lastName text)
    
    ''')
    conn.commit()


def add_user(userId: int, nick: str, firstName: str, lastName: str) :
    conn = get_connection()
    c = conn.cursor()
    c.execute('INSERT INTO users (userId, nick,firstName,lastName) VALUES (?, ?, ?, ?)', (userId, nick, firstName, lastName))
    conn.commit()


def check(userId: int) :
    conn = get_connection()
    c = conn.cursor()
    c.execute('SELECT EXISTS (SELECT userId FROM users WHERE userId = ?) ', (userId,))
    rows = c.fetchone()
    row = rows[0]
    return row


def delete_user(userId: int, nick: str, firstName: str, lastName: str) :
    conn = get_connection()
    c = conn.cursor()
    c.execute('DELETE FROM users (userId, nick, firstName, lastName) VALUE(?,?,?,?)'), (userId, nick, firstName, lastName)
    conn.commit()


def users_to_send():
    conn = get_connection()
    c = conn.cursor()
    c.execute('SELECT nick FROM users')
    rows = c.fetchall()
    rows=[i[0] for i in rows]
    return rows
