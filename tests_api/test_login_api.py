import requests

URL = "https://reqres.in/api/users?page=2"

response = requests.get(URL)
print(response.status_code)
print(response.json())
