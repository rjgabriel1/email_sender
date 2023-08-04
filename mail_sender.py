import smtplib
import ssl
import os
from dotenv import load_dotenv
load_dotenv()

def send_email(subject, email_body, mailing_list=None):
    
    # create a connection to the Gmail server
    host = os.getenv("HOST")
    port = os.getenv('PORT')
    username = os.getenv("USERNAME")
    password = os.getenv('PASSWORD')
    context = ssl.create_default_context()
  
    if mailing_list:
        receivers = mailing_list
    else:
        receivers = "gabrieljeffersonralph@gmail.com"
        
    # Format the message to have subject and body
    message = f"""\
Subject:{subject}

{email_body}
"""
    with smtplib.SMTP_SSL(host=host, port=port, context=context) as server:
        try:
            server.login(username, password)
            server.sendmail(username, receivers, message)
        except smtplib.SMTPException as ERROR:
            print("Unable to send email.",ERROR)


if __name__ == "__main__":
    send_email("Just a test..", "Trying something with python.")