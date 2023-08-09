import os
import requests
from mail_sender import send_email
api_key = os.getenv("API_KEY")

topic="ios"
url =f"https://newsapi.org/v2/everything?q={topic}&sortBy=publishedAt&apiKey={api_key}&language=en"

# Make a request
r = requests.get(url=url, timeout=60)
# Get dictionary of data
data = r.json()
articles_list= data["articles"]

def load_mailing_list(filename):
    """
    Load email addresses from a file.
    Args:
        filename (str): Name of the file containing email addresses.
    Returns:
        list: List of email addresses without leading/trailing whitespace.
    """
    try:
        with open(filename, encoding='utf-8') as emails:
            return [email.strip() for email in emails]
    except FileNotFoundError as file_error:
        print("Missing email list:", file_error)
        return []



mailing_list = load_mailing_list("email_list.txt")



# Access the articles title,description and url and create email body
body = ""
for article in articles_list[:20]:
    title = article["title"]
    if title is not None:
       body += f"{title}\n{article['url']}\n\n"
 

send_email(email_body=body, receiver=mailing_list)
