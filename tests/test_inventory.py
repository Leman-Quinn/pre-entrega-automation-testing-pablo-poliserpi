from pages.login_page import LogingPage
from pages.inventory_page import InventoryPage
import logging

####################################################################################################
# Consigna 2: Navegación y Verificación del Catálogo
# Caso de Prueba de Navegación:
# Verificar que el título de la página de inventario sea correcto
# Comprobar que existan productos visibles en la página (al menos verificar la presencia de uno)
# Validar que elementos importantes de la interfaz estén presentes (menú, filtros, etc.)
####################################################################################################
# Criterios mínimos:
# Valida título
# Valida presencia de productos
# Lista nombre/precio del primero.
####################################################################################################


def test_titulo_de_pagina(driver, credenciales_validas):
    login_page = LogingPage(driver)
    login_page.abrir().login_completo(*credenciales_validas)

    inventory_page_sub_title = InventoryPage(driver).obtener_subtitulo()

    assert inventory_page_sub_title == "Products"
