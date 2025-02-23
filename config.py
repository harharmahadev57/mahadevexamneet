import mysql.connector

SECRET_KEY = "7d07b2e7b3c4d364d3a8dde0dc4b7c71f8f3d6600c09f9e3f0d1acf7a095437"

# ✅ सबसे पहले MySQL कनेक्शन डिटेल्स को सही तरीके से डिफाइन करें
MYSQL_HOST = "localhost"
MYSQL_USER = "root"
MYSQL_PASSWORD = "mahadev@5757"
MYSQL_DB = "exam_db"

# ✅ अब MySQL सर्वर से कनेक्ट करें
db = mysql.connector.connect(
    host=MYSQL_HOST,
    user=MYSQL_USER,
    password=MYSQL_PASSWORD,
    database=MYSQL_DB
)

cursor = db.cursor()
