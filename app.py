from flask import Flask, render_template, request, redirect, url_for, session
import cloudinary.uploader
import os

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # सुरक्षा के लिए कोई भी strong key डालें

# **Cloudinary Configuration (config.py इंपोर्ट करें)**
import config

# **फिक्स्ड एडमिन लॉगिन डिटेल्स**
ADMIN_EMAIL = "karanvachhani47@gmail.com"
ADMIN_PASSWORD = "Alpha7777"

# **स्टूडेंट लॉगिन डाटा (डेमो के लिए Dictionary में रखा है, इसे Database में स्टोर कर सकते हैं)**
students = {
    "student1@gmail.com": "student123",
    "student2@gmail.com": "password456"
}

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    email = request.form['email']
    password = request.form['password']
    user_type = request.form['user_type']  # **यह बताएगा कि लॉगिन Admin है या Student**

    if user_type == "admin":
        if email == ADMIN_EMAIL and password == ADMIN_PASSWORD:
            session['user'] = "admin"
            return redirect(url_for('admin_dashboard'))
        else:
            return "Invalid Admin Credentials! Please try again."

    elif user_type == "student":
        if email in students and students[email] == password:
            session['user'] = "student"
            return redirect(url_for('student_dashboard'))
        else:
            return "Invalid Student Credentials! Please try again."

    return redirect(url_for('home'))

@app.route('/admin_dashboard')
def admin_dashboard():
    if session.get('user') == "admin":
        return render_template("admin_dashboard.html")
    else:
        return redirect(url_for('home'))

@app.route('/student_dashboard')
def student_dashboard():
    if session.get('user') == "student":
        return render_template("student_dashboard.html")
    else:
        return redirect(url_for('home'))

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('home'))

# **📌 Exam PDF Upload Feature**
@app.route("/upload_exam", methods=["POST"])
def upload_exam():
    if session.get('user') != "admin":
        return redirect(url_for('home'))

    if "exam_pdf" not in request.files:
        return "No file uploaded", 400

    pdf_file = request.files["exam_pdf"]
    if pdf_file.filename == "":
        return "No selected file", 400

    # Upload to Cloudinary
    result = cloudinary.uploader.upload(pdf_file, resource_type="raw")
    pdf_url = result["secure_url"]

    return f"Exam Uploaded! View Here: <a href='{pdf_url}' target='_blank'>{pdf_url}</a>"

@app.route("/upload_exam_page")
def upload_exam_page():
    if session.get('user') == "admin":
        return render_template("upload.html")
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
