import requests
import pytest

headers = {"x-api-key": "free_user_3FsrRrHPqheBwC9km1N1nhcpZb8"}
body = {"email": "eve.holt@reqres.in", "password": "cityslicka"}


def test_login_api():
    response = requests.post("https://reqres.in/api/login", headers=headers, json=body)

    assert response.status_code() == 200
