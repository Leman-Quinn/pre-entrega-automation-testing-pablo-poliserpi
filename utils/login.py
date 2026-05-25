from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Funcion auxiliar para automatizacion de login
def login(driver):
    wait = WebDriverWait(driver, 5)

    # captura  usuario con espera explicita
    username_input = wait.until(EC.presence_of_element_located((By.ID, "user-name")))
    # envia teclas
    username_input.send_keys("standard_user")

    # captura  password con espera explicita
    password_input = wait.until(EC.presence_of_element_located((By.ID, "password")))
    # envia teclas
    password_input.send_keys("secret_sauce")

    # captura boton con espera explicita
    boton_login = wait.until(EC.presence_of_element_located((By.ID, "login-button")))
    # hace click sobre el boton
    boton_login.click()
