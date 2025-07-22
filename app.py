from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

# Homepage: display all items
@app.route('/')
def index():
    conn = get_db_connection()
    items = conn.execute('SELECT * FROM clothing').fetchall()
    conn.close()
    return render_template('index.html', items=items)

# Add clothing (form GET + POST)
@app.route('/add', methods=['GET', 'POST'])
def add_item():
    if request.method == 'POST':
        name = request.form['name']
        category = request.form['category']
        image_url = request.form['image_url']

        conn = get_db_connection()
        conn.execute('INSERT INTO clothing (name, category, image_url) VALUES (?, ?, ?)',
                     (name, category, image_url))
        conn.commit()
        conn.close()

        return redirect('/')
    return render_template('add.html')

