import requests
import pytest

URL = "https://reqres.in/api/users?page=1"
headers = {"x-api-key": "free_user_3FsrRrHPqheBwC9km1N1nhcpZb8"}


def test_login():
    response = requests.get(URL, headers=headers)

    data = response.json()

    print(response.status_code)
    # print(data["data"])

    for entry in range(len(data["data"])):
        print(data["data"][entry])

        assert "id" in data["data"][entry], "falta campo id"
        assert "email" in data["data"][entry], "falta campo email"
        assert "first_name" in data["data"][entry], "falta campo first_name"
        assert "last_name" in data["data"][entry], "falta campo last_name"
