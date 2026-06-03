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


def test_carrito(login_handler):
    driver = login_handler

    boton_agregar_al_carrito = driver.find_element(
        By.ID, "add-to-cart-sauce-labs-backpack"
    )

    boton_agregar_al_carrito.click()

    badge_carrito = driver.find_element(By.CLASS_NAME, "shopping_cart_badge")

    assert badge_carrito.text == "1"

    link_carrito = driver.find_element(By.CLASS_NAME, "shopping_cart_link")

    link_carrito.click()

    assert (
        "/cart.html" in driver.current_url
    ), "-- Redireccion inventario a carrito fallida"

    nombre_item_en_carrito = driver.find_element(By.CLASS_NAME, "inventory_item_name")
    precio_item_en_carrito = driver.find_element(By.CLASS_NAME, "inventory_item_price")

    assert (nombre_item_en_carrito.text == "Sauce Labs Backpack") and (
        precio_item_en_carrito.text == "$29.99"
    )


####################################################################################################
# Generar reporte en HTML de las pruebas realizadas:
# pytest pre-entrega-final/test_saucedemo.py -v --html=reporte.html
####################################################################################################
