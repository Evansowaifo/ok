from fastapi import FastAPI, Form
from fastapi.responses import JSONResponse
import smtplib
from email.mime.text import MIMEText
import os

app = FastAPI()

EMAIL = os.getenv("GMAIL_EMAIL")
APP_PASSWORD = os.getenv("GMAIL_APP_PASSWORD")

@app.post("/send")
def send_email(
    name: str = Form(...),
    email: str = Form(...),
    subject: str = Form(...),
    comment: str = Form(...)
):
    msg = MIMEText(f"Name: {name}\nEmail: {email}\n\nMessage:\n{comment}")
    msg["Subject"] = subject
    msg["From"] = email
    msg["To"] = "evanskiba05@gmail.com"

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(EMAIL, APP_PASSWORD)
    server.send_message(msg)
    server.quit()

    return JSONResponse({"message": "Email sent successfully"})