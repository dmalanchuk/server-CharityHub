from email.message import EmailMessage
from aiosmtplib import SMTP

import os
from dotenv import load_dotenv

load_dotenv()

SMTP_USER = os.getenv("SMTP_USER")
SMTP_PASS = os.getenv("SMTP_PASS")

SMTP_HOST = "smtp.gmail.com"
SMTP_PORT = 587



async def send_verification_code(code: str, to_email: str):
    msg = EmailMessage()
    msg["FROM"] = SMTP_USER
    msg["TO"] = to_email
    msg["SUBJECT"] = "Verify your email"
    msg.set_content(f"Your verification code is: {code}")

    smtp = SMTP(
        hostname=SMTP_HOST,
        port=SMTP_PORT,
        use_tls=False
    )

    await smtp.connect()
    await smtp.starttls()
    await smtp.login(SMTP_USER, SMTP_PASS)
    await smtp.send_message(msg)
    await smtp.quit()

