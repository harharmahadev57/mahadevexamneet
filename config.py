import psycopg2

# 🔑 Secret Key (अगर जरूरत हो)
SECRET_KEY = "7d07b2e7b3c4d364d3a8dde0dc4b7c71f8f3d6600c09f9e3f0d1acf7a095437"

# ✅ PostgreSQL Database Connection Details (From Render)
DB_HOST = "dpg-cutfgqbtq21c73bemns0-a"
DB_PORT = "5432"
DB_NAME = "exam_db_848p"
DB_USER = "exam_db_848p_user"
DB_PASSWORD = "4KtEKvxuF6R4LkQZAiUimku8EkgBLqZs"

try:
    # ✅ Connect to PostgreSQL Database
    db = psycopg2.connect(
        host=DB_HOST,
        port=DB_PORT,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD
    )
    
    cursor = db.cursor()
    
    
