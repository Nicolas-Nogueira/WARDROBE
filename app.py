from flask import Flask, render_template, request, redirect
import sqlite3
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)

UPLOAD_FOLDER = 'static/uploads'
ALLOWED_EXTENSIONS = {'pdf', 'jpg', 'jpeg'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

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
        file = request.files['file']
        file_path = None
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            if not os.path.exists(app.config['UPLOAD_FOLDER']):
                os.makedirs(app.config['UPLOAD_FOLDER'])
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)

        conn = get_db_connection()
        conn.execute('INSERT INTO clothing (name, category, file_path) VALUES (?, ?, ?)',
                     (name, category, file_path))
        conn.commit()
        conn.close()

        return redirect('/')
    return render_template('add.html')

