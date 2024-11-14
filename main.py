import requests
from pyexpat.errors import messages

from send_email import send_email

api_key = "cfd20fd5084140928eb847fc033e450d"
topic = "tesla"

url = ("https://newsapi.org/v2/everything?"
       f"q={topic}&"
       "sortBy=publishedAt&"
       "apiKey=cfd20fd5084140928eb847fc033e450d&"
       "language=en")

request = requests.get(url)
content = request.json()
subject = "Subject: Today`s news" + "\n"
body = ""
for article in content["articles"][:20]:
       body = (body + article["title"] + "\n"
               + article["description"] + "\n"
               + article["url"] + 2*"\n")

message = (subject + body).encode("utf-8")
send_email(message)

