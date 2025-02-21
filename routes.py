from flask import Flask, request, jsonify, render_template, session
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token, jwt_required, JWTManager
from db import mysql, app
from models import create_tables

app.config["JWT_SECRET_KEY"] = "supersecretkey"
jwt = JWTManager(app)

# Create Database Tables
create_tables()

@app.route("/admin/login", methods=["POST"])
def admin_login():
    data = request.json
    email = data.get("email")
    password = data.get("password")

    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM admin WHERE email = %s", (email,))
    admin = cursor.fetchone()
    cursor.close()

    if admin and check_password_hash(admin[2], password):
        access_token = create_access_token(identity=email)
        return jsonify({"token": access_token}), 200
    else:
        return jsonify({"error": "Invalid credentials"}), 401

@app.route("/student/login", methods=["POST"])
def student_login():
    data = request.json
    phone = data.get("phone_number")
    
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM students WHERE phone_number = %s", (phone,))
    student = cursor.fetchone()
    cursor.close()

    if student:
        access_token = create_access_token(identity=phone)
        return jsonify({"token": access_token}), 200
    else:
        return jsonify({"error": "Student not found"}), 404
