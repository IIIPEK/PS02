import requests
from pprint import pprint

params = {"q": "html",}

response = requests.get("https://api.github.com/search/repositories", params=params)

if response.status_code == 200:
    result = response.json()
    print(f'{"=" * 50}\nGET request was successful with status code: {response.status_code}\n{"-" * 50}')
    print(f'Total repositories HTML type in GitHub are: {result["total_count"]}')
else:
    print(response.status_code)

params = {"userId": "1",}

response = requests.get("https://jsonplaceholder.typicode.com/posts", params=params)

if response.status_code == 200:
    result = response.json()
    print(f'{"=" * 50}\nGET request was successful with status code: {response.status_code}\n{"-" * 50}')
    pprint(result)
else:
    print(response.status_code)

data = {"title": "foo", "body": "bar", "userId": 1}

response = requests.post("https://jsonplaceholder.typicode.com/posts", data=data)

if response.status_code == 201:
    result = response.json()
    print(f'{"="*50}\nPOST request was successful with status code: {response.status_code}\n {}\n{"-" * 50}')
    print(result)
    pprint(result)
else:
    print(response.status_code)
