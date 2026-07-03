import requests
import pytest
from utils.logger import logger

####################################################################
# Caso de Prueba API 3: Crear usuarios de API
# 1. Emitir un POST con usuarios válidos falsos a la API
# 2. Verificar que las entradas creaciones hayan sido exitosas
####################################################################

# se define la URL en una constante
URL = "https://reqres.in/api/users"

# se define la api key en una constante
headers = {"x-api-key": "free_user_3FsrRrHPqheBwC9km1N1nhcpZb8"}

# se establece un array con usuarios falsos para testeo
FAKE_USERS = [
    ("7", "fakemail7@reqres.in", "fakename7", "fakelastname7", "fakeavatar7"),
    ("8", "fakemail8@reqres.in", "fakename8", "fakelastname8", "fakeavatar8"),
    ("9", "fakemail9@reqres.in", "fakename9", "fakelastname9", "fakeavatar9"),
]


# decorator para ciclar datos
@pytest.mark.parametrize("id, email, first_name, last_name, avatar", FAKE_USERS)
def test_create_users(id, email, first_name, last_name, avatar):
    logger.info("Inicio de test_api_create_user.py::test_create_users")

    # se define el body a emitir
    body = {
        "id": id,
        "email": email,
        "first_name": first_name,
        "last_name": last_name,
        "avatar": avatar,
    }

    # se emite un POST a la API
    response = requests.post(URL, headers=headers, json=body)

    # se evalua la respuesta inmediata
    assert response.status_code == 201, "Error: status code esperado incorrecto"
    logger.info(f"Status code recibido correcto: {response.status_code}")

    # se almacena el body de la respuesta
    data = response.json()

    # se evalua que los datos creados coincidan con los emitidos
    assert (
        data["id"] == body["id"]
    ), "Error: campo id enviado no coincide con campo id creado"
    assert (
        data["email"] == body["email"]
    ), "Error: campo email enviado no coincide con campo email creado"
    assert (
        data["first_name"] == body["first_name"]
    ), "Error: campo first_name enviado no coincide con campo first_name creado"
    assert (
        data["last_name"] == body["last_name"]
    ), "Error: campo last_name enviado no coincide con campo last_name creado"
    assert (
        data["avatar"] == body["avatar"]
    ), "Error: campo avatar enviado no coincide con campo avatar creado"
    assert (
        "2026" in data["createdAt"]
    ), "Error: campo createdAt esperado no coincide con campo createdAt obtenido"

    logger.info("Creación de usuarios exitosa")

    logger.info("Fin de test_api_create_user.py::test_create_users")
