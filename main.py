from fastapi import FastAPI, Request, Form, Depends, HTTPException from fastapi.templating import Jinja2Templates from fastapi.staticfiles import StaticFiles from fastapi.middleware.cors import CORSMiddleware from pathlib import Path import os import jwt import datetime from dotenv import load_dotenv

.env फाइल को लोड करें

load_dotenv() SECRET_KEY = os.getenv("SECRET_KEY", "defaultsecret")

app = FastAPI()

टेम्पलेट्स और स्टैटिक फाइल्स की लोकेशन सेट करें

BASE_DIR = Path(file).resolve().parent templates = Jinja2Templates(directory=str(BASE_DIR / "templates")) app.mount("/static", StaticFiles(directory="static"), name="static")

CORS Middleware

app.add_middleware( CORSMiddleware, allow_origins=[""],  # सभी डोमेन को अनुमति देता है (प्रोडक्शन में इसे Specific करें) allow_credentials=True, allow_methods=[""], allow_headers=["*"], )

Dummy Database (इसे असली DB से रिप्लेस करें)

users_db = {"karan57@gmail.com": "k1234"}

एडमिन लॉगिन पेज दिखाने के लिए रूट

@app.get("/admin/login") def admin_login(request: Request): return templates.TemplateResponse("adminlogin.html", {"request": request})

स्टूडेंट लॉगिन पेज दिखाने के लिए रूट

@app.get("/student/login") def student_login(request: Request): return templates.TemplateResponse("studentlogin.html", {"request": request})

लॉगिन पेज दिखाने के लिए रूट

@app.get("/login") def login_page(request: Request): return templates.TemplateResponse("login.html", {"request": request})

लॉगिन API (POST)

@app.post("/login") def login(email: str = Form(...), password: str = Form(...)): if email in users_db and users_db[email] == password: token = jwt.encode({"email": email, "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=2)}, SECRET_KEY, algorithm="HS256") return {"message": "Login successful", "token": token} else: raise HTTPException(status_code=401, detail="Invalid Credentials")

होम API

@app.get("/") def home(): return {"message": "FastAPI is running!"}

FastAPI सर्वर रन करना

import uvicorn if name == "main": port = int(os.environ.get("PORT", 5000))  # Render पर PORT ऑटो-सेट होता है uvicorn.run(app, host="0.0.0.0", port=port)
