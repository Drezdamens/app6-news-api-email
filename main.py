import requests

api_key = "cfd20fd5084140928eb847fc033e450d"

url = ("https://newsapi.org/v2/everything?q=tesla"
       "&from=2024-10-13&sortBy=publishedAt&apiKey=cfd20fd5084140928eb847fc033e450d")

request = requests.get(url)
content = request.json()

for article in content["articles"]:
       print(article["title"])
       print(article["description"])