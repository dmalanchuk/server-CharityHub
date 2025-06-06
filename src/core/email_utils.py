from email.message import EmailMessage
from aiosmtplib import SMTP
import ssl

import os
from dotenv import load_dotenv

load_dotenv()

SMTP_USER = os.getenv("SMTP_USER")
SMTP_PASS = os.getenv("SMTP_PASS")

SMTP_HOST = "smtp.gmail.com"
SMTP_PORT = 587


async def send_verification_code(code: str, to_email: str):
    ssl_context = ssl.create_default_context()

    msg = EmailMessage()
    msg["From"] = SMTP_USER
    msg["To"] = to_email
    msg["Subject"] = "Verify your email"
    msg.set_content(f"Your verification code is: {code}")

    try:
        async with SMTP(
                hostname=SMTP_HOST,
                port=SMTP_PORT,
                start_tls=True,
                tls_context=ssl_context,
                timeout=10
        ) as smtp:
            await smtp.login(SMTP_USER, SMTP_PASS)
            await smtp.send_message(msg)

        return True
    except Exception as e:
        print(f"Failed to send email: {str(e)}")
        return False

