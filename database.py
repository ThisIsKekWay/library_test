import sqlite3


def init():
    connection = sqlite3.connect('library.db')

    cursor = connection.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            author INTEGER NOT NULL,
            year INTEGER NOT NULL CHECK (year >= 1900),
            status INTEGER NOT NULL
            )
        ''')

    connection.commit()

    connection.close()
