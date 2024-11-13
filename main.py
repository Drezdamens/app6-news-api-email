import requests
from send_email import send_email

api_key = "cfd20fd5084140928eb847fc033e450d"

url = ("https://newsapi.org/v2/everything?q=tesla"
       "&from=2024-10-13&sortBy=publishedAt&apiKey=cfd20fd5084140928eb847fc033e450d")

request = requests.get(url)
content = request.json()
body = ""
for article in content["articles"]:
       body = body + article["title"] + "\n" + article["description"] + 2*"\n"

body = body.encode("utf-8")
send_email(body)

