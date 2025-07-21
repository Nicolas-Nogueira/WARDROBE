import sqlite3

conn = sqlite3.connect("database.db")
c = conn.cursor()

c.execute('''
CREATE TABLE clothing (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    category TEXT NOT NULL,
    image_url TEXT
)
''')

conn.commit()
conn.close()
