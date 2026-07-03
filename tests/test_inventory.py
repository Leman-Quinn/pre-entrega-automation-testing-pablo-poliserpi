from pages.login_page import LogingPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from utils.logger import logger

#######################################################################################################
# Caso de Prueba 2: Navegación y Verificación de Catálogo
# 1. Acceder al sitio con credeciales válidas
# 2. Verificar que el título de la pagina de inventario sea correcto
# 3. Comprobar que existen productos visibles en la página verificando la existencia de al menos uno
#######################################################################################################


def test_titulo_de_pagina(driver, credenciales_validas):
    logger.info("Inicio de test_inventory.py::test_titulo_de_pagina")

    # se instancia LogingPage pasandole driver
    login_page = LogingPage(driver)

    # se abre la pagina demo y se logea con credenciales validas
    logger.info(f"Accediendo a sitio web con credenciales validas")
    login_page.abrir().login_completo(*credenciales_validas)

    # se accede a la pagina de inventario
    inventory_page = InventoryPage(driver)

    sub_title = inventory_page.obtener_subtitulo()

    # se evalua el titulo secundario
    logger.info("Evaluando titulo secundario")
    assert sub_title == "Products", "Titulo secundario incorrecto"
    logger.info("Titulo secundario correcto")

    logger.info("Fin de test_titulo_de_pagina.py")


def test_existencia_productos(driver, credenciales_validas):
    logger.info("Inicio de test_inventory.py::test_existencia_producto")

    # se instancia LogingPage pasandole driver
    login_page = LogingPage(driver)

    # se abre la pagina demo y se logea con credenciales validas
    logger.info(f"Accediendo al sitio web con credenciales validas")
    login_page.abrir().login_completo(*credenciales_validas)

    # se abre la pagina de inventario
    inventory_page = InventoryPage(driver)

    logger.info(f"Capturando primer bloque con productos")
    productos = inventory_page.obtener_productos()

    logger.info(f"Contenido del primer bloque: {productos[0].text}")

    logger.info("Fin de test_inventory.py::test_existencia_producto")
