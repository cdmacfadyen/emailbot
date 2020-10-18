from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os
import smtplib, ssl, email


class EmailBot:
  email_address = ""
  account_name = ""
  
  def __init__(self, recipient, bot_identifier):
    self.email_address = recipient
    self.bot_identifier = bot_identifier

  def get_password(self):
    with open(os.path.expanduser("~/.emailbot")) as f:
      for line in f:
        if self.bot_identifier in line:
          tokens = line.split("\t")
          tokens = [token.rstrip() for token in tokens]
          print(tokens)
          print(tokens[1:])
          return tokens[1:]

  def email_me(self, message="Task Complete", subject="Task Complete"):
      port = 465

      username, password = self.get_password()
      context = ssl.create_default_context()

      with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
          msg = MIMEMultipart()
          msg["From"] = username
          msg["To"] = self.email_address
          msg["Subject"] = subject

          body = message
          msg.attach(MIMEText(body, "plain"))
          server.login(username, password)
          server.sendmail(username, self.email_address, msg.as_string() )