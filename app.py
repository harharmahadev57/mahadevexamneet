from flask import Flask, request, jsonify, session, redirect, url_for, render_template
import mysql.connector
import cloudinary
import cloudinary.uploader

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # सुरक्षा के लिए कोई भी strong key डालें

# **Cloudinary Configuration**
cloudinary.config(
    cloud_name="your_cloud_name",
    api_key="your_api_key",
    api_secret="your_api_secret"
)

# **Database Connection**
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="yourpassword",
    database="exam_db"
)
cursor = conn.cursor()

# **Admin Login Credentials (Fixed)**
ADMIN_CREDENTIALS = {
    "email": "karanvachhani47@gmail.com",
    "password": "Alpha7777"
}

# **Demo Student Data (Later, Store in DB)**
students = {
    "student1@gmail.com": "student123",
    "student2@gmail.com": "password456"
}

# **Home Route**
@app.route('/')
def home():
    return render_template('login.html')

# **Login Route**
@app.route('/login', methods=['POST'])
def login():
    email = request.form['email']
    password = request.form['password']
    user_type = request.form['user_type']  # Admin or Student

    if user_type == "admin":
        if email == ADMIN_CREDENTIALS["email"] and password == ADMIN_CREDENTIALS["password"]:
            session['user'] = "admin"
            return redirect(url_for('admin_dashboard'))
        else:
            return "Invalid Admin Credentials!", 401

    elif user_type == "student":
        if email in students and students[email] == password:
            session['user'] = "student"
            return redirect(url_for('student_dashboard'))
        else:
            return "Invalid Student Credentials!", 401

    return redirect(url_for('home'))

# **Admin Dashboard**
@app.route('/admin_dashboard')
def admin_dashboard():
    if session.get('user') == "admin":
        return render_template('admin_dashboard.html')
    return redirect(url_for('home'))

# **Student Dashboard**
@app.route('/student_dashboard')
def student_dashboard():
    if session.get('user') == "student":
        return render_template('student_dashboard.html')
    return redirect(url_for('home'))

# **Logout Route**
@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('home'))

# **Run App**
if __name__ == '__main__':
    app.run(debug=True)
