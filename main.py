import os
import requests
from dotenv import load_dotenv

api_key = os.getenv("API_KEY")

url ="https://newsapi.org/v2/everything?q=tesla&from=2023-07-04&sortBy=publishedAt&apiKey=79d7ebd73e3f4e2aaef7d9490612644e"

# Make a request
r = requests.get(url)
# Get dictionary of data
data = r.json()
articles_list= data["articles"]

# Access the articles title,description and url
for article in articles_list:
    print(article["title"])
    print(article["description"])
    print(article["url"]+'\n')


with open("email_list.txt") as emails:
    mailing_list = [email.replace("\n","") for email in emails.readlines()]


 