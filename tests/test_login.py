from selenium.webdriver.common.by import By

####################################################################################################
# Consigna 1: Automatización de Login
# Navegar a la página de login de saucedemo.com
# Ingresar credenciales válidas (usuario: "standard_user", contraseña: "secret_sauce")
# Validar login exitoso verificando que se haya redirigido a la página de inventario
####################################################################################################
# Criterios mínimos:
# Login automatizado con espera explícita y validación de /inventory.html y “Products/Swag Labs”.
####################################################################################################


def test_login_validation(login_handler):
    driver = login_handler

    assert "/inventory.html" in driver.current_url, "-- Redireccion de login fallida"

    titulo_principal = driver.find_element(By.CLASS_NAME, "app_logo")

    assert titulo_principal.text == "Swag Labs", "-- Titulo principal incorrecto"

    titulo_secundario = driver.find_element(
        By.CSS_SELECTOR, "div.header_secondary_container .title"
    )

    assert titulo_secundario.text == "Products", "-- Titulo secundario incorrecto"


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


def test_inventory(login_handler):
    driver = login_handler

    items_inventario = driver.find_elements(By.CLASS_NAME, "inventory_item")

    assert len(items_inventario) >= 1

    icono_menu = driver.find_element(By.ID, "react-burger-menu-btn")

    assert icono_menu.is_displayed() == True

    filtro_desplegable = driver.find_element(By.CLASS_NAME, "product_sort_container")

    assert filtro_desplegable.is_displayed() == True

    badge_carrito = driver.find_element(By.CLASS_NAME, "shopping_cart_link")

    assert badge_carrito.is_displayed() == True

    nombre_primer_producto = driver.find_element(By.CLASS_NAME, "inventory_item_name ")
    precio_primer_producto = driver.find_element(By.CLASS_NAME, "inventory_item_price ")

    print(f"++ Nombre Primer Producto: {nombre_primer_producto.text}")
    print(f"++ Precio Primer Producto: {precio_primer_producto.text}")


####################################################################################################
# Interacción con Productos: (Clase 8)
# Caso de Prueba de Carrito:
# Añadir un producto al carrito haciendo clic en el botón correspondiente
# Verificar que el contador del carrito se incremente correctamente
# Navegar al carrito de compras
# Comprobar que el producto añadido aparezca correctamente en el carrito
####################################################################################################
# Criterios mínimos:
# Agrega primer producto
# Verifica ítem en carrito.
####################################################################################################

####################################################################################################
# Repositorio en GitHub:
# Sube el proyecto a un repositorio en GitHub
# Realiza commits frecuentes y con mensajes descriptivos que muestren el progreso del proyecto
####################################################################################################
# README.md:
# Incluye un archivo README.md que explique:
# El propósito del proyecto
# Las tecnologías utilizadas
# Cómo instalar las dependencias
# Cómo ejecutar las pruebas
####################################################################################################
# Generar reporte en HTML de las pruebas realizadas:
# pytest pre-entrega-final/test_saucedemo.py -v --html=reporte.html
####################################################################################################
