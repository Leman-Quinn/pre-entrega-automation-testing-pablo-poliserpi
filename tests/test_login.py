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
    login_page = LogingPage(driver)
    login_page.abrir().login_completo(*credenciales_validas)

    inventory_page_main_title = InventoryPage(driver)

    assert inventory_page_main_title.obtener_titulo() == "Swag Labs"
