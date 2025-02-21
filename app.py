app.py (Main Flask Application)

from flask import Flask, render_template, request, redirect, url_for, session from flask_mysqldb import MySQL import MySQLdb.cursors import re

app = Flask(name) app.secret_key = 'your_secret_key'

Database Configuration

app.config['MYSQL_HOST'] = 'your-mysql-host' app.config['MYSQL_USER'] = 'root' app.config['MYSQL_PASSWORD'] = 'mahadev@5757' app.config['MYSQL_DB'] = 'exam_db'

mysql = MySQL(app)

Route: Home

@app.route('/') def home(): return render_template('index.html')

Route: Admin Login

@app.route('/admin', methods=['GET', 'POST']) def admin_login(): if request.method == 'POST': email = request.form['email'] password = request.form['password'] if email == 'karanvachhani47@gmail.com' and password == 'Alpha777': session['admin_loggedin'] = True return redirect(url_for('admin_dashboard')) return render_template('admin_login.html')

Route: Admin Dashboard

@app.route('/admin/dashboard') def admin_dashboard(): if 'admin_loggedin' in session: return render_template('admin_dashboard.html') return redirect(url_for('admin_login'))

Route: Student Login

@app.route('/student', methods=['GET', 'POST']) def student_login(): if request.method == 'POST': phone = request.form['phone'] password = request.form['password'] cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor) cursor.execute('SELECT * FROM students WHERE phone_number = %s AND password = %s', (phone, password)) student = cursor.fetchone() if student: session['student_loggedin'] = True session['student_id'] = student['id'] return redirect(url_for('student_dashboard')) return render_template('student_login.html')

Route: Student Dashboard

@app.route('/student/dashboard') def student_dashboard(): if 'student_loggedin' in session: return render_template('student_dashboard.html') return redirect(url_for('student_login'))

if name == 'main': app.run(debug=True)
