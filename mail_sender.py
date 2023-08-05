import os
import smtplib
import ssl
from email.message import EmailMessage
from dotenv import load_dotenv
load_dotenv()

def send_email(email_body: str, subject: str =None,  receiver:list | str =None):
    """
    Send an Email
    :param subject: Email subject
    :param  email_body: Content of the mail
    :param receiver: Receipient it can be a list or a string
    """
    
    # create a connection to the Gmail server
    host = os.getenv("HOST")
    port = os.getenv('PORT')
    username = os.getenv("USERNAME")
    password = os.getenv('PASSWORD')
    context = ssl.create_default_context()
  
    if receiver:
        email_to = receiver
    else:
        email_to = "gabrieljeffersonralph@gmail.com"
        
    if subject:
        subject=subject
    else:
        subject="Today's News"
    # Format the message to have subject and body
#         message = f"""\
# Subject:{subject}

# {email_body}
# """
    em = EmailMessage()
    em.set_content(email_body)
    em["To"]= email_to
    em["From"]= username
    em["Subject"]= subject
    

    with smtplib.SMTP_SSL(host=host, port=port, context=context) as server:
        try:
            server.login(username, password)
            server.send_message(em)
        except smtplib.SMTPException as ERROR:
            print("Unable to send email.",ERROR)


if __name__ == "__main__":
    send_email("Just a test..", "Trying something with python.")