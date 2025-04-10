import smtplib
from email.message import EmailMessage
from dotenv import load_dotenv
import os


class SendMail:
    def __init__(self):
        load_dotenv()
        self.smtp_address = os.getenv("SMTP_ADDRESS")
        self.email_address = os.getenv("EMAIL_ADDRESS")
        self.password = os.getenv("EMAIL_PASSWORD")

    def send_to(self, condition, subject, content):
        if condition:
            msg = EmailMessage()
            msg.set_content(content)
            msg['Subject'] = subject
            msg['From'] = self.email_address
            msg['To'] = "oluwafemiakinode909@yahoo.com"
            with smtplib.SMTP_SSL(self.smtp_address, 465) as connection:
                connection.login(user=self.email_address, password=self.password)
                connection.send_message(msg)
