import requests
import pytest
from utils.datos import leer_csv_login_api
from utils.logger import logger

####################################################################
# Caso de Prueba API 1: Acceso a API
# 1. Emitir un POST con credenciales validas e invalidas a la API
# 2. Verificar que los casos hayan sido exitosos
####################################################################

# se define la URL en una constante
URL = "https://reqres.in/api/login"
# se define la api key en una constante
headers = {"x-api-key": "free_user_3FsrRrHPqheBwC9km1N1nhcpZb8"}
# se cargan los casos de login externos
CASOS_LOGIN_API = leer_csv_login_api("datos/api_login.csv")


# decorator para ciclar casos de login
@pytest.mark.parametrize("email, password, debe_funcionar", CASOS_LOGIN_API)
def test_login(email, password, debe_funcionar):
    logger.info("Inicio de test_api_login.py::test_login")

    # se crea el body
    body = {"email": email, "password": password}

    # se emite un POST a ReqRes
    response = requests.post(URL, headers=headers, json=body)

    # se evalua el resultado del caso
    if debe_funcionar:
        assert response.status_code == 200, "Error: código de status distinto a 200"
    else:
        assert response.status_code == 400, "Error: código de status distinto a 400"

    logger.info("Fin de test_api_login.py::test_login")
