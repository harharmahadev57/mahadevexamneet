import mysql.connector

db = mysql.connector.connect(
    SECRET_KEY = "81d744702ecb4accadeba0f85bec5f61"
    MYSQL_HOST = "karan-LOQ-15IAX9"
    MYSQL_USER = "root"
    MYSQL_PASSWORD = "mahadev@5757"
    MYSQL_DB = "exam_db"

)
cursor = db.cursor()
