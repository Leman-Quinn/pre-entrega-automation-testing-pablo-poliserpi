from pages.login_page import LogingPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
import logging

####################################################################################################
# Consigna 3: Interacción con Productos
# Caso de Prueba de Carrito
# Añadir un producto al carrito haciendo clic en el botón correspondiente
# Verificar que el contador del carrito se incremente correctamente
# Navegar al carrito de compras
# Comprobar que el producto añadido aparezca correctamente en el carrito
####################################################################################################
# Criterios mínimos:
# Agrega primer producto
# Verifica ítem en carrito.
####################################################################################################


def test_agregar_producto(driver, credenciales_validas):
    logger = logging.getLogger(__name__)

    login_page = LogingPage(driver)
    login_page.abrir().login_completo(*credenciales_validas)

    inventory_page = InventoryPage(driver)

    primer_producto = inventory_page.agregar_primer_producto()
    contador_carrito = inventory_page.obtener_contador_carrito()

    logger.info(f"Cantidad de items en carrito: {contador_carrito}")

    cart_page = inventory_page.ir_al_carrito()

    nombre_primer_producto = cart_page.obtener_nombres_productos()
    precio_primer_producto = cart_page.obtener_precios_productos()

    logger.info(f"Nombre Esperado del Item: Sauce Labs Backpack")
    logger.info(f"Precio Esperado del Item: 29.99")
    logger.info(f"Nombre Registrado del Item: {nombre_primer_producto}")
    logger.info(f"Precio Registrado del Item: {precio_primer_producto}")

    assert contador_carrito >= 1
