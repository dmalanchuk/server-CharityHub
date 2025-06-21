import smtplib
import threading
import os

from email.message import EmailMessage
from dotenv import load_dotenv
from src.core.get_email_text import get_email_text

load_dotenv()

SMTP_USER = os.getenv("SMTP_USER")
SMTP_PASS = os.getenv("SMTP_PASS")


def send_email_sync(msg):
    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.login(SMTP_USER, SMTP_PASS)
            smtp.send_message(msg)
    except Exception as e:
        print(f"Email send failed: {e}")



def send_verification_code_sync(code, to_email):

    text = get_email_text(code, path="src/templates/email_temp_txt.txt")
    html = get_email_text(code, path="src/templates/email_temp_html.html")

    msg = EmailMessage()
    msg["From"] = SMTP_USER
    msg["To"] = to_email
    msg["Subject"] = "Verify your email"
    msg["List-Unsubscribe"] = f"<mailto:{SMTP_USER}>"
    msg["Reply-To"] = SMTP_USER
    msg.set_content(text)
    msg.add_alternative(html, subtype="html")

    thread = threading.Thread(target=send_email_sync, args=(msg,))
    thread.start()
