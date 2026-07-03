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

# carga credenciales primero
CASOS_LOGIN = leer_csv_login("datos/login.csv")


# decorator para ciclar sets de datos automaticamente
@pytest.mark.parametrize("usuario, clave, debe_funcionar", CASOS_LOGIN)
def test_login(driver, usuario, clave, debe_funcionar):
    # se instancia un log
    logger = logging.getLogger(__name__)

    # se instancia clase de LoginPage pasandole driver
    login_page = LogingPage(driver)
    # se abre la pagina demo y se logea
    login_page.abrir().login_completo(usuario, clave)

    # se instancia clase de InventoryPage con pasandole driver
    inventory_page = InventoryPage(driver)

    # if para separar distintos flujos segun credenciales
    if debe_funcionar:
        # se captura el titulo
        main_title = inventory_page.obtener_titulo()

        # se guarda en log el esperado y el obtenido
        logger.info(f"Título principal esperado: Swag Labs")
        logger.info(f"Título principal encontrado: {main_title}")

        # se evalua el titulo
        assert main_title == "Swag Labs"
    else:
        # se chequea que haya dado mensaje de error
        assert "Happy" in login_page.obtener_mensaje_error()
        # assert "Epic sadface" in login_page.obtener_mensaje_error()
