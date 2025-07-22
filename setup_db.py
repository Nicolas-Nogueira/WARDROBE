import sqlite3

conn = sqlite3.connect('database.db')
c = conn.cursor()

# Drop table to start fresh
c.execute('DROP TABLE IF EXISTS clothing')

# Create table
c.execute('''
CREATE TABLE clothing (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    category TEXT NOT NULL,
    file_path TEXT,
    is_favorite INTEGER DEFAULT 0
)
''')

conn.commit()
conn.close()

