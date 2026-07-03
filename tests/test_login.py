from pages.login_page import LogingPage
from pages.inventory_page import InventoryPage
from utils.datos import leer_csv_login
import pytest
from utils.logger import logger

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
    logger.info("Inicio de test_login.py")

    # se instancia clase de LoginPage pasandole driver
    login_page = LogingPage(driver)

    logger.info("Accediendo al sitio web")
    # se abre la pagina demo y se logea
    login_page.abrir().login_completo(usuario, clave)

    # se instancia clase de InventoryPage con pasandole driver
    inventory_page = InventoryPage(driver)

    # if para separar distintos flujos segun credenciales
    if debe_funcionar:
        logger.info("Credenciales correctas")
        logger.info("Evaluando titulo principal")
        # se captura el titulo
        main_title = inventory_page.obtener_titulo()

        # se evalua el titulo
        assert main_title == "Swag Labs", "Titulo incorrecto"
        if main_title == "Swag Labs":
            logger.info("Titulo correcto")
    else:
        # se chequea que haya dado mensaje de error
        logger.info("Credenciales incorrectas")
        logger.info("Evaluando mensaje de acceso denegado")
        assert (
            "Epic sadface" in login_page.obtener_mensaje_error()
        ), "Mensaje de acceso denegado incorrecto"
        if "Epic sadface" in login_page.obtener_mensaje_error():
            logger.info("Mensaje de acceso denegado correcto")

    logger.info("Fin de test_login.py")
