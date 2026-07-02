import requests
import pytest

URL = "https://reqres.in/api/users"
headers = {"x-api-key": "free_user_3FsrRrHPqheBwC9km1N1nhcpZb8"}
FAKE_USERS = [
    ("7", "fakemail7@reqres.in", "fakename7", "fakelastname7", "fakeavatar7"),
    ("8", "fakemail8@reqres.in", "fakename8", "fakelastname8", "fakeavatar8"),
    ("9", "fakemail9@reqres.in", "fakename9", "fakelastname9", "fakeavatar9"),
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

    assert response.status_code == 201

    data = response.json()

    assert data["id"] == body["id"]
    assert data["email"] == body["email"]
    assert data["first_name"] == body["first_name"]
    assert data["last_name"] == body["last_name"]
    assert data["avatar"] == body["avatar"]
    assert "2026" in data["createdAt"]
