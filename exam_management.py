from flask import Flask, render_template, request, redirect, url_for, session
import sqlite3

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Database Connection
def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

# Admin Dashboard - Manage Exams
@app.route('/manage_exams')
def manage_exams():
    if 'admin' not in session:
        return redirect(url_for('admin_login'))
    
    conn = get_db_connection()
    exams = conn.execute('SELECT * FROM exams').fetchall()
    conn.close()
    
    return render_template('manage_exams.html', exams=exams)

# Add New Exam
@app.route('/add_exam', methods=['POST'])
def add_exam():
    if 'admin' not in session:
        return redirect(url_for('admin_login'))
    
    name = request.form['name']
    date = request.form['date']
    duration = request.form['duration']

    conn = get_db_connection()
    conn.execute('INSERT INTO exams (name, date, duration) VALUES (?, ?, ?)', (name, date, duration))
    conn.commit()
    conn.close()

    return redirect(url_for('manage_exams'))

# Delete Exam
@app.route('/delete_exam/<int:exam_id>')
def delete_exam(exam_id):
    if 'admin' not in session:
        return redirect(url_for('admin_login'))
    
    conn = get_db_connection()
    conn.execute('DELETE FROM exams WHERE id = ?', (exam_id,))
    conn.commit()
    conn.close()

    return redirect(url_for('manage_exams'))

if __name__ == '__main__':
    app.run(debug=True)
