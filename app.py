from flask import Flask, render_template, request, session, redirect, url_for
import random
import smtplib

app = Flask(__name__)
app.secret_key = "your_secret_key"

# Dummy Admin और Student Data (इसे बाद में डेटाबेस से जोड़ा जा सकता है)
ADMIN_EMAIL = "admin@example.com"
STUDENT_DATA = {"student1@example.com": "password123"}  
ADMIN_OTP = None  # OTP स्टोर करने के लिए

@app.route("/", methods=["GET", "POST"])
def login():
    global ADMIN_OTP
    if request.method == "POST":
        user_type = request.form["user_type"]
        email = request.form["email"]
        password = request.form.get("password")

        if user_type == "admin":
            ADMIN_OTP = random.randint(100000, 999999)
            send_email(email, ADMIN_OTP)
            session["admin_email"] = email
            return redirect(url_for("admin_verify"))
        elif user_type == "student":
            if email in STUDENT_DATA and STUDENT_DATA[email] == password:
                session["student_logged_in"] = True
                return redirect(url_for("student_dashboard"))
            else:
                return "Invalid Student Credentials!"
    return render_template("login.html")

@app.route("/admin_verify", methods=["GET", "POST"])
def admin_verify():
    if request.method == "POST":
        otp = request.form["otp"]
        if int(otp) == ADMIN_OTP:
            session["admin_logged_in"] = True
            return redirect(url_for("admin_dashboard"))
        else:
            return "Invalid OTP!"
    return render_template("admin_verify.html")

@app.route("/admin_dashboard")
def admin_dashboard():
    if not session.get("admin_logged_in"):
        return redirect(url_for("login"))
    return "Welcome, Admin!"

@app.route("/student_dashboard")
def student_dashboard():
    if not session.get("student_logged_in"):
        return redirect(url_for("login"))
    return "Welcome, Student!"

def send_email(to_email, otp):
    sender_email = "your-email@gmail.com"
    sender_password = "your-email-password"
    
    message = f"Your OTP is {otp}"
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(sender_email, sender_password)
    server.sendmail(sender_email, to_email, message)
    server.quit()

if __name__ == "__main__":
    app.run(debug=True)
