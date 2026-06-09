from pages.login_page import LogingPage
from pages.inventory_page import InventoryPage
from utils.datos import leer_csv_login
import pytest
import logging

####################################################################################################
# Consigna 1: Automatización de Login
# Navegar a la página de login de saucedemo.com
# Ingresar credenciales válidas (usuario: "standard_user", contraseña: "secret_sauce")
# Validar login exitoso verificando que se haya redirigido a la página de inventario
####################################################################################################
# Criterios mínimos:
# Login automatizado con espera explícita y validación de /inventory.html y “Products/Swag Labs”.
####################################################################################################


@pytest.mark.parametrize(
    "usuario, clave, debe_funcionar", leer_csv_login("datos/login.csv")
)
def test_login(driver, usuario, clave, debe_funcionar):
    logger = logging.getLogger(__name__)

    login_page = LogingPage(driver)
    login_page.abrir().login_completo(usuario, clave)

    inventory_page = InventoryPage(driver)

    if debe_funcionar:
        main_title = inventory_page.obtener_titulo()

        logger.info(f"Título principal esperado: Swag Labs")
        logger.info(f"Título principal encontrado: {main_title}")

        assert main_title == "Swag Labs"
    else:
        assert login_page.obtener_mensaje_error()
