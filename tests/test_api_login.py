import requests
import pytest
from utils.datos import leer_csv_login_api

headers = {"x-api-key": "free_user_3FsrRrHPqheBwC9km1N1nhcpZb8"}
CASOS_LOGIN_API = leer_csv_login_api("datos/api_login.csv")


@pytest.mark.parametrize("email, password, debe_funcionar", CASOS_LOGIN_API)
def test_login(email, password, debe_funcionar):
    body = {"email": email, "password": password}

    response = requests.post("https://reqres.in/api/login", headers=headers, json=body)

    if debe_funcionar:
        assert response.status_code == 200
    else:
        assert response.status_code == 400
