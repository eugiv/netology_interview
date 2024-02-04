import json
import email
import smtplib
import imaplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

GMAIL_SMTP = "smtp.gmail.com"
GMAIL_IMAP = "imap.gmail.com"


class SendMails:
    def __init__(self, e_mail: str, password: str):
        self.e_mail = e_mail
        self.password = password


if __name__ == "__main__":
    with open("sensitive.txt") as f:
        file = json.loads(f.read())
        user_email = file["user_1"]["email"]
        user_password = file["user_1"]["password"]

    user_inst_1 = SendMails(user_email, user_password)
