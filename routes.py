from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_user, logout_user, login_required
from models import db, Student

app = Flask(__name__)
app.config.from_object('config.Config')

db.init_app(app)

login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return Student.query.get(int(user_id))

@app.route("/")
def home():
    return render_template("login.html")

@app.route("/login", methods=["POST"])
def login():
    email = request.form["email"]
    password = request.form["password"]
    user = Student.query.filter_by(email=email, password=password).first()
    if user:
        login_user(user)
        return redirect(url_for("dashboard"))
    else:
        flash("Invalid email or password", "danger")
        return redirect(url_for("home"))

@app.route("/dashboard")
@login_required
def dashboard():
    return render_template("dashboard.html")

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(debug=True)


from flask import jsonify
from models import Exam
from datetime import datetime

@app.route("/create_exam", methods=["POST"])
def create_exam():
    data = request.json
    new_exam = Exam(
        exam_name=data["exam_name"],
        exam_date=datetime.strptime(data["exam_date"], "%Y-%m-%d"),
        question_paper=data["question_paper"],
        answer_key=data["answer_key"]
    )
    db.session.add(new_exam)
    db.session.commit()
    return jsonify({"message": "Exam Created Successfully!"}), 201  



@app.route("/submit_exam", methods=["POST"])
@login_required
def submit_exam():
    data = request.json
    exam_id = data["exam_id"]
    answers = data["answers"]
    
    exam = Exam.query.get(exam_id)
    correct_answers = exam.answer_key.split(",")  
    score = sum(1 for i, ans in enumerate(answers) if ans == correct_answers[i])
    
    result = Result(
        student_id=current_user.id,
        exam_id=exam_id,
        marks=score,
        total_marks=len(correct_answers),
        result_status="Pass" if score > (0.4 * len(correct_answers)) else "Fail"
    )
    db.session.add(result)
    db.session.commit()
    return jsonify({"message": "Exam Submitted!"}), 200


@app.route("/result_analysis")
@login_required
def result_analysis():
    results = Result.query.all()
    data = [{"student_id": r.student_id, "exam_id": r.exam_id, "marks": r.marks, "status": r.result_status} for r in results]
    return jsonify(data)


from models import Admin
from flask import request, jsonify
from flask_login import login_user

@app.route("/admin_login", methods=["POST"])
def admin_login():
    data = request.json
    email = data.get("email")  # यूजर से ईमेल लेना
    password = data.get("password")  # यूजर से पासवर्ड लेना
    
    admin = Admin.query.filter_by(email=email, password=password).first()
    
    if admin:
        login_user(admin)
        return jsonify({"message": "Admin Logged In"}), 200
    return jsonify({"error": "Invalid Credentials"}), 401


from flask import Flask, request, jsonify, session
from werkzeug.security import check_password_hash
import psycopg2

app = Flask(__name__)
app.secret_key = "your_secret_key"

# Database Connection
def get_db_connection():
    return psycopg2.connect(
        dbname="exam_db", user="exam_user", password="your_password", host="your_host"
    )

@app.route('/admin/login', methods=['POST'])
def admin_login():
    data = request.json
    username = data.get('username')
    password = data.get('password')

    conn = get_db_connection()
    cur = conn.cursor()
    
    cur.execute("SELECT id, password FROM admins WHERE username = %s", (username,))
    admin = cur.fetchone()
    
    if admin and check_password_hash(admin[1], password):
        session['admin_id'] = admin[0]
        return jsonify({"message": "Login Successful", "admin_id": admin[0]}), 200
    else:
        return jsonify({"error": "Invalid Credentials"}), 401

