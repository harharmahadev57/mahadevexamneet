from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import jwt
import datetime

app = FastAPI()

# Dummy Database (इसे असली DB से रिप्लेस करें)
users_db = {"karan57@gmail.com": "k1234"}

# लॉगिन डेटा के लिए मॉडल
class LoginRequest(BaseModel):
    email: str
    password: str

# लॉगिन API
@app.post("/admin")
def login(user: LoginRequest):
    if user.email in users_db and users_db[user.email] == user.password:
        token = jwt.encode({"email": user.email, "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=2)}, "secret", algorithm="HS256")
        return {"message": "Login successful", "token": token}
    else:
        raise HTTPException(status_code=401, detail="Invalid Credentials")

import os
from dotenv import load_dotenv

# .env फाइल को लोड करें
load_dotenv()

# SECRET_KEY को एक्सेस करें
SECRET_KEY = os.getenv("81d744702ecb4accadeba0f85bec5f61")

print("SECRET_KEY:", SECRET_KEY)  
