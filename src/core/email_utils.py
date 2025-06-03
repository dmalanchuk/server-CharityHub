from email.message import EmailMessage
from aiosmtplib import SMTP


SMTP_HOST = "sandbox.smtp.mailtrap.io"
SMTP_PORT = 587
SMTP_USER = "95a1307be86e18"
SMTP_PASS = "7de596792ef732"


async def send_verification_email(code: str, to_email: str):
    msg = EmailMessage()
    msg["FROM"] = "noreply@charityhub.com"
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

