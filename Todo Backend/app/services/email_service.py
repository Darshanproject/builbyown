import random

from fastapi_mail import FastMail
from fastapi_mail import MessageSchema
from fastapi_mail import MessageType

from app.core.mail import conf


class EmailService:

    @staticmethod
    async def send_otp(email: str, otp: str):

        message = MessageSchema(
            subject="Todo App Verification",
            recipients=[email],
            body=f"""
Your verification code is:

<h2>{otp}</h2>

Valid for 5 minutes.
""",
            subtype=MessageType.html
        )

        fm = FastMail(conf)

        await fm.send_message(message)

   
   
    @staticmethod
    async def send_email(email: str, subject: str, body: dict,template: str):
        message = MessageSchema(
            subject=subject,
            recipients=[email],
            subtype=MessageType.html
        )

        fm = FastMail(conf)
        await fm.send_message(message,
        template_name=template)