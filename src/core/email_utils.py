from email.message import EmailMessage
import smtplib
import threading

import os
from dotenv import load_dotenv

load_dotenv()

SMTP_USER = os.getenv("SMTP_USER")
SMTP_PASS = os.getenv("SMTP_PASS")


def send_email_sync(msg):
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(SMTP_USER, SMTP_PASS)
        smtp.send_message(msg)



def send_verification_code_sync(code, to_email):

    body = f"""\
    Hi!

    Your verification code is: {code}

    If you did not request this, please ignore this email.

    Best regards,
    MyApp Team
    """

    html = f"""\
    <html>
      <body>
        <p>Hi!</p>
        <p>Your verification code is: <strong>{code}</strong></p>
        <p>If you did not request this, please ignore this email.</p>
        <p>Best regards,<br>CharityHub Team</p>
      </body>
    </html>
    """

    msg = EmailMessage()
    msg["From"] = SMTP_USER
    msg["To"] = to_email
    msg["Subject"] = "Verify your email"
    msg["List-Unsubscribe"] = f"<mailto:{SMTP_USER}>"
    msg["Reply-To"] = SMTP_USER
    msg.set_content(body)
    msg.add_alternative(html, subtype="html")

    thread = threading.Thread(target=send_email_sync, args=(msg,))
    thread.start()
