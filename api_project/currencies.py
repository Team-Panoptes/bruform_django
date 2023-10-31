import requests
import json

url = "https://api.frankfurter.app/2023-10-01..2023-10-31?to=USD"

r = requests.get(url)

data = json.loads(r.text)

eur_to_usd = []
for date, rate in data["rates"].items():
    eur_to_usd.append(rate["USD"])

print(eur_to_usd)
