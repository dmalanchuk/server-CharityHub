from email.message import EmailMessage

import aiosmtplib

async def send_email(from_email: str, to_email: str, subject: str, body: str):

    msg = EmailMessage()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject
    msg.set_content(body)

    await aiosmtplib.send(
        ...
    )
