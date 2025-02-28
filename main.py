import requests
from pprint import pprint

params = {"q": "html",}

response = requests.get("https://api.github.com/search/repositories", params=params)

if response.status_code == 200:
    result = response.json()
    print(f'Total repositories HTML type: {result["total_count"]}')
else:
    print(response.status_code)