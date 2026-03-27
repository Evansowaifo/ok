from fastapi import FastAPI, Form
from fastapi.responses import JSONResponse
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
import os

app = FastAPI()

SENDGRID_API_KEY = os.getenv("SENDGRID_API_KEY")  # set in Render env
FROM_EMAIL = "evanskiba05@gmail.com"  # verified sender
TO_EMAIL = "evansowaifo@gmail.com"    # fixed recipient

@app.post("/send")
def send_email(
    name: str = Form(...),
    email: str = Form(...),
    subject: str = Form(...),
    comment: str = Form(...)
):
    # user email appears in the message body
    content = f"Name: {name}\nEmail: {email}\n\nMessage:\n{comment}"
    
    message = Mail(
        from_email=FROM_EMAIL,  # always evanskiba05@gmail.com
        to_emails=TO_EMAIL,
        subject=subject,
        plain_text_content=content
    )
    
    try:
        sg = SendGridAPIClient(SENDGRID_API_KEY)
        sg.send(message)
        return JSONResponse({"message": "Email sent successfully"})
    except Exception as e:
        return JSONResponse({"error": str(e)}, status_code=500)