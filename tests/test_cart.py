from pages.login_page import LogingPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from utils.datos import leer_csv_login
from utils.datos import leer_json_productos
import pytest
from utils.logger import logger

#########################################################
# Caso de Prueba UI 3: Interacción con Productos
# 1. Añadir un producto al carrito haciendo clic en el botón correspondiente
# 2. Verificar que el contador del carrito se incremente correctamente
# 3. Navegar al carrito de compras
# 4. Comprobar que el producto añadido aparezca correctamente en el carrito
#########################################################

# carga de productos
LISTA_PRODUCTOS = leer_json_productos("datos/productos.json")


def test_agregar_producto(driver, credenciales_validas):
    logger.info("Inicio de test_cart.py::test_agregar_producto")

    # se instancia LoginPage pasandole driver
    login_page = LogingPage(driver)

    # se abre la pagina demo y se logea con credenciales validas
    logger.info(f"Accediendo a sitio web con credenciales validas")
    login_page.abrir().login_completo(*credenciales_validas)

    # se instancia clase de InventoryPage pasandole driver
    inventory_page = InventoryPage(driver)

    # se obtiene un array con los productos en la pagina
    for producto in LISTA_PRODUCTOS:
        inventory_page.agregar_producto_por_nombre(producto)

    # se obtiene contador de carrito
    contador_carrito = inventory_page.obtener_contador_carrito()

    # se instancia CartPage
    cart_page = inventory_page.ir_al_carrito()

    # se capturan nombres y precios de productos en carrito
    nombres_productos = cart_page.obtener_nombres_productos()
    precios_productos = cart_page.obtener_precios_productos()
    logger.info(f"Nombre(s) esperado del/los item(s): {LISTA_PRODUCTOS}")
    logger.info(f"Nombre(s) encontrado del/los item(s): {nombres_productos}")
    logger.info(f"Precio(s) esperado del/los item(s): $29.99, $9.99, $15.99")
    logger.info(f"Precio(s) encontrado del/los item(s): {precios_productos}")

    logger.info("Evaluando cantidad de items en carrito")
    assert contador_carrito >= 1, "Error: Contador de items en carrito < 1"
    logger.info(f"Cantidad de items en carrito: {contador_carrito}")

    logger.info("Fin de test_cart.py::test_agregar_producto")
