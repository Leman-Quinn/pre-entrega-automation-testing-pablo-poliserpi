import requests
import pytest
from utils.logger import logger

####################################################################################
# Caso de Prueba API 4: Creacion, edicion y delecion de entrada (JSONPlaceHolder)
# 1. Emitir un POST con entrada nueva
# 2. Verificar que la entrada hayan sido creada exitosamente
####################################################################################

# se define la URL en una constante
URL_POST = "https://jsonplaceholder.typicode.com/posts"

# se define un body para el POST
POST_BODY = {
    "userId": "20",
    "id": "",
    "title": "Random title",
    "body": "Random long text",
}

# se define la URL en una constante
URL_PATCH = "https://jsonplaceholder.typicode.com/posts/22"

# se define una payload para el PATCH
PATCH_PAYLOAD = {"title": "A different random tittle"}


def test_post():
    logger.info("Inicio de test_post_lifecyle.py::test_post")

    # se emite un POST
    response = requests.post(URL_POST, json=POST_BODY)

    # se evalua respuesta inmediata
    assert response.status_code == 201, "Error: código de status recibido incorrecto"
    logger.info(f"Status code recibido correcto: {response.status_code}")

    # se guarda el body de la respuesta
    data = response.json()

    # se evalua que el id de la entrada creada coincida con el esperado (101 en este caso para JSONPlaceHolder)
    received_id = data["id"]
    assert received_id == 101, "Error: campo id esperado incorrecto"
    logger.info(f"campo id recibido correcto: {received_id}")

    # se evalua el tiempo de respuesta
    assert (
        response.elapsed.total_seconds() < 2
    ), "Error: tiempo de respuesta superior a 2 segundos"
    logger.info("Tiempo de respuesta: < 2 segundos")

    logger.info("Fin de test_post_lifecyle.py::test_post")


def test_patch():
    logger.info("Inicio de test_post_lifecyle.py::test_patch")

    # se emite un PATCH
    response = requests.patch(URL_PATCH, json=PATCH_PAYLOAD)

    # se evalua la respuesta inmediata
    assert response.status_code == 200, "Error: código de status recibido incorrecto"
    logger.info(f"Status code recibido correcto: {response.status_code}")

    # se guarda el body de la respuesta
    data = response.json()

    # se evalua que el titulo se haya editado
    assert (
        data["title"] == PATCH_PAYLOAD["title"]
    ), "Error: campo titulo creado no coincide con campo titulo enviado"
    logger.info("Edición de entrada exitosa")

    # se evalua tiempo de respuesta
    assert (
        response.elapsed.total_seconds() < 1
    ), "Error: tiempo de respuesta superior a 1 segundo"
    logger.info("Tiempo de respuesta: < 1 segundos")

    logger.info("Fin de test_post_lifecyle.py::test_patch")


def test_delete():
    logger.info("Inicio de test_post_lifecyle.py::test_delete")

    # se emite un DELETE
    response = requests.delete(URL_PATCH)

    # se evalua la respuesta inmediata, 200 para JSONPlaceHolder en caso de DELETE
    assert response.status_code == 200, "Error: código de status recibido incorrecto"
    logger.info(f"Status code recibido correcto: {response.status_code}")

    # se evalua el tiempo de respuesta
    assert (
        response.elapsed.total_seconds() < 1
    ), "Error: tiempo de respuesta superior a 1 segundo"
    logger.info("Tiempo de respuesta: < 1 segundos")

    logger.info("Fin de test_post_lifecyle.py::test_delete")
