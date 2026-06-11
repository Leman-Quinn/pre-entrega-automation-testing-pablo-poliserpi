from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class InventoryPage:

    # atributos
    _TITLE = (By.CLASS_NAME, "app_logo")
    _SUBTITLE = (By.CLASS_NAME, "title")
    _PRODUCTS = (By.CLASS_NAME, "inventory_item")
    _ADD_BUTTONS = (By.CSS_SELECTOR, "button[data-test*='add-to-cart']")
    _CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    _CART_LINK = (By.CLASS_NAME, "shopping_cart_link")
    _MENU_BUTTON = (By.ID, "react-burger-menu-btn")
    _LOGOUT_LINK = (By.ID, "logout_sidebar_link")

    # constructor
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # metodos
    def obtener_titulo(self):
        return self.driver.find_element(*self._TITLE).text

    def obtener_subtitulo(self):
        return self.driver.find_element(*self._SUBTITLE).text

    def obtener_productos(self):
        return self.driver.find_elements(*self._PRODUCTS)

    def agregar_primer_producto(self):
        primer_boton = self.driver.find_elements(*self._ADD_BUTTONS)[0]
        primer_boton.click()

        return self

    def agregar_producto_por_nombre(self, nombre_producto):
        arr_bloques = self.driver.find_elements(*self._PRODUCTS)

        for bloque in arr_bloques:
            nombre_bloque = bloque.find_element(By.CLASS_NAME, "inventory_item_name")

            if nombre_bloque.text == nombre_producto:
                boton_agregar = self.driver.find_element(*self._ADD_BUTTONS)
                boton_agregar.click()

        return self

    def obtener_contador_carrito(self):
        try:
            badge = self.driver.find_element(*self._CART_BADGE)

            return int(badge.text)
        except:
            return 0

    def ir_al_carrito(self):
        self.driver.find_element(*self._CART_LINK).click()

        # lazy import to avoid circular dependencies
        from pages.cart_page import CartPage

        return CartPage(self.driver)

    def hacer_logout(self):
        self.driver.find_element(*self._MENU_BUTTON).click()
        logout_link = self.wait.until(EC.element_to_be_clickable(self._LOGOUT_LINK))
        logout_link.click()
        from pages.login_page import LoginPage

        return LoginPage(self.driver)
