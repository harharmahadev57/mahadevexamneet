from flask import Flask, render_template, request, redirect, url_for, session
from flask_mysqldb import MySQL
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from config import Config
import MySQLdb.cursors

app = Flask(__name__)
app.config.from_object(Config)

mysql = MySQL(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

class User(UserMixin):
    def __init__(self, id, username, user_type):
        self.id = id
        self.username = username
        self.user_type = user_type

@login_manager.user_loader
def load_user(user_id):
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute("SELECT id, username, 'admin' as user_type FROM admins WHERE id = %s UNION SELECT id, phone_number as username, 'student' as user_type FROM students WHERE id = %s", (user_id, user_id))
    user = cursor.fetchone()
    if user:
        return User(id=user['id'], username=user['username'], user_type=user['user_type'])
    return None

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        user_type = request.form['user_type']
        username = request.form['username']
        password = request.form['password']
        hashed_password = generate_password_hash(password)

        cursor = mysql.connection.cursor()
        if user_type == 'admin':
            cursor.execute("INSERT INTO admins (username, password_hash) VALUES (%s, %s)", (username, hashed_password))
        elif user_type == 'student':
            cursor.execute("INSERT INTO students (phone_number, password_hash) VALUES (%s, %s)", (username, hashed_password))
        mysql.connection.commit()
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user_type = request.form['user_type']
        username = request.form['username']
        password = request.form['password']

        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        if user_type == 'admin':
            cursor.execute("SELECT * FROM admins WHERE username = %s", (username,))
        elif user_type == 'student':
            cursor.execute("SELECT * FROM students WHERE phone_number = %s", (username,))
        user = cursor.fetchone()

        if user and check_password_hash(user['password_hash'], password):
            user_obj = User(id=user['id'], username=username, user_type=user_type)
            login_user(user_obj)
            if user_type == 'admin':
                return redirect(url_for('admin_dashboard'))
            else:
                return redirect(url_for('student_dashboard'))
        else:
            return "Invalid credentials"
    return render_template('login.html')

@app.route('/admin/dashboard')
@login_required
def admin_dashboard():
    if current_user.user_type != 'admin':
        return "Unauthorized", 403
    return f"Welcome to the Admin Dashboard, {current_user.username}!"

@app.route('/student/dashboard')
@login_required
def student_dashboard():
    if current_user.user_type != 'student':
        return "Unauthorized", 403
    return f"Welcome to the Student Dashboard, {current_user.username}!"

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
