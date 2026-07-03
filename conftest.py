import pytest
from selenium import webdriver
import time
import pathlib


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


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield

    report = outcome.get_result()

    if report.when == "call" and report.failed:
        driver = item.funcargs.get("driver")

        if driver:
            target = pathlib.Path("reports/screenshots")
            target.mkdir(parents=True, exist_ok=True)

            file_name = target / f"{item.name}.png"

            driver.save_screenshot(str(file_name))
