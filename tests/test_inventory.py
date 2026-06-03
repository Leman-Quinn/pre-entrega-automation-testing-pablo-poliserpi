from pages.login_page import LogingPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
import logging

####################################################################################################
# Consigna 2: Navegación y Verificación del Catálogo
# Caso de Prueba de Navegación:
# Verificar que el título de la página de inventario sea correcto
# Comprobar que existan productos visibles en la página (al menos verificar la presencia de uno)
# Validar que elementos importantes de la interfaz estén presentes (menú, filtros, etc.)
####################################################################################################
# Criterios mínimos:
# Valida título
# Valida precesencia de produtos
# Lista nombre/precio del primero.
####################################################################################################


def test_titulo_de_pagina(driver, credenciales_validas):
    logger = logging.getLogger(__name__)

    login_page = LogingPage(driver)
    login_page.abrir().login_completo(*credenciales_validas)

    inventory_page = InventoryPage(driver)
    sub_title = inventory_page.obtener_subtitulo()

    logger.info(f"Título secundario esperado: Products")
    logger.info(f"Título secundario encontrado: {sub_title}")

    assert sub_title == "Products"


def test_existencia_productos(driver, credenciales_validas):
    logger = logging.getLogger(__name__)

    login_page = LogingPage(driver)
    login_page.abrir().login_completo(*credenciales_validas)

    inventory_page = InventoryPage(driver)

    productos = inventory_page.obtener_productos()

    logger.info(f"Contenido del primer bloque: {productos[0].text}")
