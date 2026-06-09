import pytest
from selenium import webdriver
import time


@pytest.fixture(scope="function")
def driver():
    """Fixture que proporciona un WebDriver configurado."""
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.implicitly_wait(5)

    yield driver

    time.sleep(1)  # Para ver el resultado final
    driver.quit()


# DEPRECATED - DO NOT USE
@pytest.fixture(scope="session")
def credenciales_validas():

    usuario = "standard_user"
    clave = "secret_sauce"

    return usuario, clave


# DEPRECATED - DO NOT USE
@pytest.fixture(scope="session")
def credenciales_invalidas():

    usuario = "standard_user"
    clave = "12345"

    return usuario, clave


# DEPRECATED - DO NOT USE
@pytest.fixture(scope="session")
def usuario_bloqueado():

    usuario = "locked_out_user"
    clave = "secret_sauce"

    return usuario, clave
