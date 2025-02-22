from flask import Flask, render_template, request, redirect, url_for, session
from flask_mysqldb import MySQL
import MySQLdb.cursors
import os

# Flask App Initialize
app = Flask(__name__)
app.secret_key = 'your_secret_key'  # 🔑 Change this for security

# Database Configurations
app.config['MYSQL_HOST'] = 'your_mysql_host'
app.config['MYSQL_USER'] = 'your_mysql_user'
app.config['MYSQL_PASSWORD'] = 'your_mysql_password'
app.config['MYSQL_DB'] = 'your_database_name'

mysql = MySQL(app)

# Home Route
@app.route('/')
def home():
    return render_template('index.html')

# Admin Login Route
@app.route('/admin', methods=['GET', 'POST'])
def admin_login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        
        # ✅ Admin credentials updated
        if email == 'karanvachhani47@gmail.com' and password == 'Alpha777':
            session['admin_loggedin'] = True
            return redirect(url_for('admin_dashboard'))
        
    return render_template('admin_login.html')

# Admin Dashboard Route
@app.route('/admin/dashboard')
def admin_dashboard():
    if 'admin_loggedin' in session:
        return render_template('admin_dashboard.html')
    return redirect(url_for('admin_login'))

# Student Login Route
@app.route('/student', methods=['GET', 'POST'])
def student_login():
    if request.method == 'POST':
        phone = request.form['phone']
        password = request.form['password']
        
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM students WHERE phone_number = %s AND password = %s', (phone, password))
        student = cursor.fetchone()
        
        if student:
            session['student_loggedin'] = True
            session['student_id'] = student['id']
            return redirect(url_for('student_dashboard'))
    
    return render_template('student_login.html')

# Student Dashboard Route
@app.route('/student/dashboard')
def student_dashboard():
    if 'student_loggedin' in session:
        return render_template('student_dashboard.html')
    return redirect(url_for('student_login'))

# Logout Route
@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('home'))

# Run the Flask Application
if __name__ == "__main__":
    app.run(debug=True)
