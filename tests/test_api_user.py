import requests
import pytest
from utils.logger import logger

####################################################################
# Caso de Prueba API 2: Leer usuarios de API (ReqRes)
# 1. Emitir un GET con credenciales validas a la API
# 2. Verificar que las entradas contengan todos los campos requeridos
####################################################################

# se define la URL en una constante
URL = "https://reqres.in/api/users?page=1"

# se define la api key en una constante
headers = {"x-api-key": "free_user_3FsrRrHPqheBwC9km1N1nhcpZb8"}


def test_get_users():
    logger.info("Inicio de test_api_user.py::test_get_users")

    # se emite un GET a la API
    response = requests.get(URL, headers=headers)

    # se evalua la respuesta inmediata
    assert response.status_code == 200, "Error: status code esperado incorrecto"
    logger.info(f"Status code recibido correcto: {response.status_code}")

    # se guarda el body de la respuesta
    data = response.json()

    # se cicla y evalua los campos en cada entrada recibida
    for entry in range(len(data["data"])):
        print(data["data"][entry])

        assert "id" in data["data"][entry], "falta campo id"
        assert "email" in data["data"][entry], "falta campo email"
        assert "first_name" in data["data"][entry], "falta campo first_name"
        assert "last_name" in data["data"][entry], "falta campo last_name"

    logger.info("Fin de test_api_user.py::test_get_users")
