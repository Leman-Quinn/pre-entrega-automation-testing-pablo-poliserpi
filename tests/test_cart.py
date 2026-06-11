from pages.login_page import LogingPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from utils.datos import leer_csv_login
from utils.datos import leer_json_productos
import pytest
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

# carga credenciales primero
CASOS_LOGIN = leer_csv_login("datos/login.csv")

# carga de productos
LISTA_PRODUCTOS = leer_json_productos("datos/productos.json")


# decorator para ciclar sets de datos automaticamente
@pytest.mark.parametrize("usuario, clave, debe_funcionar", CASOS_LOGIN)
def test_agregar_producto(driver, usuario, clave, debe_funcionar):
    # se instancia un log
    logger = logging.getLogger(__name__)

    # se instancia clase de LoginPage pasandole driver
    login_page = LogingPage(driver)
    # se abre la pagina demo y se logea
    login_page.abrir().login_completo(usuario, clave)

    # se instancia clase de InventoryPage con pasandole driver
    inventory_page = InventoryPage(driver)

    if debe_funcionar:
        # se obtiene un array con los productos en la pagina
        for producto in LISTA_PRODUCTOS:
            inventory_page.agregar_producto_por_nombre(producto)

        # primer_producto = inventory_page.agregar_primer_producto()

        contador_carrito = inventory_page.obtener_contador_carrito()

        logger.info(f"Cantidad de items en carrito: {contador_carrito}")

        cart_page = inventory_page.ir_al_carrito()

        nombres_productos = cart_page.obtener_nombres_productos()
        precios_productos = cart_page.obtener_precios_productos()

        logger.info(f"Nombre(s) Esperado del/los Item(s): {LISTA_PRODUCTOS}")
        logger.info(f"Precio(s) Esperado del/los Item(s): $29.99, $9.99, $15.99")
        logger.info(f"Nombre(s) Registrado del/los Item(s): {nombres_productos}")
        logger.info(f"Precio(s) Registrado del/los Item(s): {precios_productos}")

        assert contador_carrito >= 1
