import json
import email
import smtplib
import imaplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

GMAIL_SMTP = "smtp.gmail.com"
GMAIL_IMAP = "imap.gmail.com"


class SendMails:
    def __init__(self, email_address: str, password: str):
        self.email_address = email_address
        self.password = password

    def send_message(self, subject: str, recipients: list, text_message: str):
        message = MIMEMultipart()
        message["From"] = self.email_address
        message["To"] = ", ".join(recipients)
        message["Subject"] = subject
        message.attach(MIMEText(text_message))

        mail_server = smtplib.SMTP(GMAIL_SMTP, 587)
        # identify ourselves to smtp gmail client
        mail_server.ehlo()
        # secure our email with TLS encryption
        mail_server.starttls()
        # re-identify ourselves as an encrypted connection
        mail_server.ehlo()

        mail_server.login(self.email_address, self.password)
        mail_server.sendmail(self.email_address, recipients, message.as_string())

        mail_server.quit()

    def receive_message(self, receipt_mailbox="inbox", header=None):
        mail = imaplib.IMAP4_SSL(GMAIL_IMAP)
        mail.login(self.email_address, self.password)
        mail.list()
        mail.select(receipt_mailbox)

        if header:
            criterion = f'(HEADER Subject "{header}")'
        else:
            criterion = "ALL"

        data = mail.uid("search", None, criterion)
        assert data[0], "There are no letters with current header"

        latest_email_uid = data[0].split()[-1]
        data = mail.uid("fetch", latest_email_uid, "(RFC822)")
        raw_email = data[0][1]
        email.message_from_string(raw_email)

        mail.logout()


if __name__ == "__main__":
    with open("sensitive.txt", encoding="UTF8") as f:
        file_data = json.loads(f.read())
        user_email = file_data["user_1"]["email"]
        user_password = file_data["user_1"]["password"]

    user_inst_1 = SendMails(user_email, user_password)
    user_inst_1.send_message(
        "Subject", ["vasya@email.com", "petya@email.com"], "Message"
    )
    user_inst_1.receive_message()
