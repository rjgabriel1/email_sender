import os
import smtplib
import ssl
from email.message import EmailMessage
from dotenv import load_dotenv
load_dotenv()


def send_email(email_body: str, receiver: list | str = None, subject: str = None):
    """
    Send an Email
    :param subject: Email subject
    :param email_body: Content of the mail
    :param receiver: Recipient, can be a list or a string
    """

    # Set up email configuration
    host = os.getenv("HOST")
    port = os.getenv("PORT")
    username = os.getenv("USERNAME")
    password = os.getenv("PASSWORD")
    name=os.getenv("APP_NAME")
    context = ssl.create_default_context() 
    
    if receiver is not None:
        receivers = receiver
    else:
        exit("Invalid email destination", code=553)

    if subject:
        _subject = subject
    else:
        _subject = "Today's News"

    # Create and send the email
    try:
        email_message = EmailMessage()
        email_message.set_content(email_body)
        email_message.add_header("From",f'{name} <{username}>')
        email_message["Bcc"] = receivers
        email_message["Subject"] = _subject
        with smtplib.SMTP_SSL(host=host, port=port, context=context) as server:
            server.login(username, password)
            server.send_message(email_message)
    except (UnboundLocalError, smtplib.SMTPException) as error:
        print("Unable to send email.", error)



if __name__ == "__main__":
    send_email(email_body="Just a test..",receiver=["random@gmail.com", "EXAMPLE@icloud.com"],subject="Trying something with python.")