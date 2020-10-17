from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os
import smtplib, ssl, email
EMAIL = "EMAIL"

def get_password(identifier):
  with open(os.path.expanduser("SECRETS FILE")) as f:
    for line in f:
      if identifier in line:
        tokens = line.split("\t")
        tokens = [token.rstrip() for token in tokens]
        return tokens
    

def email_me(message="Task Complete"):
    port = 465

    username, password = get_password("BOT NAME")
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        msg = MIMEMultipart()
        msg["From"] = username
        msg["To"] = EMAIL
        msg["Subject"] = "Task Complete"

        body = message
        msg.attach(MIMEText(body, "plain"))
        server.login(username, password)
        server.sendmail(username, EMAIL, msg.as_string() )

