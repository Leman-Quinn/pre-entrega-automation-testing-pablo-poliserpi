from pages.login_page import LogingPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from utils.logger import logger

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
    logger.info("Inicio de test_titulo_de_pagina.py")
    login_page = LogingPage(driver)

    logger.info(f"Accediendo al sitio web con credenciales validas")
    login_page.abrir().login_completo(*credenciales_validas)

    inventory_page = InventoryPage(driver)
    sub_title = inventory_page.obtener_subtitulo()

    logger.info("Evaluando titulo secundario")
    logger.info(f"Esperado: Products")
    logger.info(f"Encontrado: {sub_title}")

    assert sub_title == "Products", "Titulo secundario incorrecto"

    if sub_title == "Products":
        logger.info(f"Titulo secundario correcto")
    else:
        logger.info(f"Titulo secundario incorrecto")

    logger.info("Fin de test_titulo_de_pagina.py")


def test_existencia_productos(driver, credenciales_validas):
    logger.info("Inicio de test_existencia_producto.py")
    login_page = LogingPage(driver)

    logger.info(f"Accediendo al sitio web con credenciales validas")
    login_page.abrir().login_completo(*credenciales_validas)

    inventory_page = InventoryPage(driver)

    productos = inventory_page.obtener_productos()

    logger.info(f"Contenido del primer bloque: {productos[0].text}")

    logger.info("Fin de test_existencia_producto.py")
