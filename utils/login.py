from selenium.webdriver.common.by import By


def login(driver):
    # captura elemento usuario
    username = driver.find_element(By.ID, "user-name")
    # presiona teclas
    username.send_keys("standard_user")

    # captura elemento password
    password = driver.find_element(By.ID, "password")
    # presiona teclas
    password.send_keys("secret_sauce")

    # captura boton
    button = driver.find_element(By.ID, "login-button")
    # hace click sobre el boton
    button.click()
