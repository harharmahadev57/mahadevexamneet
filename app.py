from flask import Flask, render_template, request, redirect, url_for, session
import psycopg2
from psycopg2.extras import DictCursor

app = Flask(__name__)

# 🔑 Secret Key for Session Management
app.secret_key = "7d07b2e7b3c4d364d3a8dde0dc4b7c71f8f3d6600c09f9e3f0d1acf7a095437"

# ✅ PostgreSQL Database Config
DB_HOST = "dpg-cutfgqbtq21c73bemns0-a"
DB_PORT = "5432"
DB_NAME = "exam_db_848p"
DB_USER = "exam_db_848p_user"
DB_PASSWORD = "4KtEKvxuF6R4LkQZAiUimku8EkgBLqZs"

# 🔌 Function to Connect to PostgreSQL
def get_db_connection():
    return psycopg2.connect(
        host=DB_HOST,
        port=DB_PORT,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD
    )

# 🏠 Home Route
@app.route('/')
def home():
    return render_template('index.html')
from flask import Flask, request, jsonify

@app.route('/admin', methods=['POST'])
def admin_login():
    data = request.get_json()  # JSON डेटा को प्राप्त करें
    if not data:
        return jsonify({"error": "Invalid JSON"}), 400

    email = data.get('email')
    password = data.get('password')

    if not email or not password:
        return jsonify({"error": "Email and password required"}), 400

    return jsonify({"message": "Login request received", "email": email}) 
            
# 🖥️ Admin Dashboard
@app.route('/admin/dashboard')
def admin_dashboard():
    if 'admin_loggedin' in session:
        return render_template('admin_dashboard.html')
    return redirect(url_for('admin_login'))

# 👨‍🎓 Student Login
@app.route('/student', methods=['GET', 'POST'])
def student_login():
    if request.method == 'POST':
        phone = request.form['phone']
        password = request.form['password']
        
        # 🔌 Connect to PostgreSQL
        conn = get_db_connection()
        cursor = conn.cursor(cursor_factory=DictCursor)

        cursor.execute('SELECT * FROM students WHERE phone_number = %s AND password = %s', (phone, password))
        student = cursor.fetchone()

        cursor.close()
        conn.close()

        if student:
            session['student_loggedin'] = True
            session['student_id'] = student['id']
            return redirect(url_for('student_dashboard'))

    return render_template('student_login.html')

# 📚 Student Dashboard
@app.route('/student/dashboard')
def student_dashboard():
    if 'student_loggedin' in session:
        return render_template('student_dashboard.html')
    return redirect(url_for('student_login'))

if __name__ == "__main__":
    app.run(debug=True)
