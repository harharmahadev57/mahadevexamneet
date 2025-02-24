import os
import jwt
import datetime
from dotenv import load_dotenv

# .env से SECRET_KEY लोड करें
load_dotenv()
SECRET_KEY = os.getenv("SECRET_KEY")

# JWT टोकन जेनरेट करने वाला फंक्शन
def generate_token(user_email):
    token = jwt.encode({"user": user_email, "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=2)}, SECRET_KEY, algorithm="HS256")
    return token

# टेस्ट के लिए एक टोकन जेनरेट करें
if __name__ == "__main__":
    user_email = "karan57@gmail.com"
    token = generate_token(user_email)
    print("Generated JWT Token:", token)
