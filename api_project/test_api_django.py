import requests
import json

r = requests.get("http://127.0.0.1:8000/books/authors")

data = json.loads(r.text)

print (data)
