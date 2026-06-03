from pages.login_page import LogingPage
from pages.inventory_page import InventoryPage
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


def test_login_exitoso_credenciales_validas(driver, credenciales_validas):
    logger = logging.getLogger(__name__)

    login_page = LogingPage(driver)
    login_page.abrir().login_completo(*credenciales_validas)

    inventory_page = InventoryPage(driver)
    main_title = inventory_page.obtener_titulo()

    logger.info(f"Título principal esperado: Swag Labs")
    logger.info(f"Título principal encontrado: {main_title}")

    assert main_title == "Swag Labs"
