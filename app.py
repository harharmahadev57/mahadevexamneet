from flask import Flask, render_template, request, redirect, url_for, session
import sqlite3

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Database Connection Function
def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

# Home Page
@app.route('/')
def home():
    return render_template('index.html')

# Student Login
@app.route('/student_login', methods=['GET', 'POST'])
def student_login():
    if request.method == 'POST':
        mobile = request.form['mobile']
        password = request.form['password']

        conn = get_db_connection()
        student = conn.execute('SELECT * FROM students WHERE mobile = ? AND password = ?', (mobile, password)).fetchone()
        conn.close()

        if student:
            session['student_id'] = student['id']
            return redirect(url_for('student_dashboard'))
        else:
            return "Invalid Credentials"

    return render_template('login.html')

# Student Dashboard
@app.route('/student_dashboard')
def student_dashboard():
    if 'student_id' not in session:
        return redirect(url_for('student_login'))
    
    return render_template('student_dashboard.html')

# Logout
@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
