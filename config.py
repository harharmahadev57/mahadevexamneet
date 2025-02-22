from dotenv import load_dotenv
import os

load_dotenv()

class Config:
    SECRET_KEY = os.getenv("81d744702ecb4accadeba0f85bec5f61")
    MYSQL_HOST = os.getenv("karan-LOQ-15IAX9")
    MYSQL_USER = os.getenv("root")
    MYSQL_PASSWORD = os.getenv("mahadev@5757")
    MYSQL_DB = os.getenv("exam_db")
