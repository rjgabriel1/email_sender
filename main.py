import os
import requests
from dotenv import load_dotenv
from mail_sender import send_email
api_key = os.getenv("API_KEY")

topic="ios"
url =f"https://newsapi.org/v2/everything?q={topic}&sortBy=publishedAt&apiKey={api_key}&language=en"

# Make a request
r = requests.get(url)
# Get dictionary of data
data = r.json()
articles_list= data["articles"]
# try:
#     with open("email_list.txt") as emails:
#         mailing_list = [email.replace("\n","") for email in emails.readlines()]
# except FileNotFoundError as e:
#     print("Missing email list",e )
    
body=""
# Access the articles title,description and url
for article in articles_list[:20]:
    if article["title"] is not None:
       body = body + article["title"] +"\n"+ article["url"]+ 2*"\n"
 
  
send_email(email_body=body, receiver="123")





 