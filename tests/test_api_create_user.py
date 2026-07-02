import requests
import pytest

URL = "https://reqres.in/api/users"
headers = {"x-api-key": "free_user_3FsrRrHPqheBwC9km1N1nhcpZb8"}
FAKE_USERS = [
    {
        "id": "7",
        "email": "fakemail7@reqres.in",
        "first_name": "fakename7",
        "last_name": "fakelastname7",
        "avatar": "fakeavatar7",
    },
    {
        "id": "8",
        "email": "fakemail8@reqres.in",
        "first_name": "fakename8",
        "last_name": "fakelastname8",
        "avatar": "fakeavatar8",
    },
    {
        "id": "9",
        "email": "fakemail9@reqres.in",
        "first_name": "fakename9",
        "last_name": "fakelastname9",
        "avatar": "fakeavatar9",
    },
]


@pytest.mark.parametrize("id, email, first_name, last_name, avatar", FAKE_USERS)
def test_login(id, email, first_name, last_name, avatar):
    body = {
        "id": id,
        "email": email,
        "first_name": first_name,
        "last_name": last_name,
        "avatar": avatar,
    }

    response = requests.post(URL, headers=headers, json=body)

    print(response.status_code)
    print(response.json())
