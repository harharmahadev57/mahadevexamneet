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
