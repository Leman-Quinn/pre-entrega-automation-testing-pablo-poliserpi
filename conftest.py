import pytest
from selenium import webdriver
from utils.login import login


# Fixtures para automatizacion de login
@pytest.fixture
def driver():
    driver = webdriver.Firefox()

    driver.get("https://www.SauceDemo.com")

    yield driver

    driver.quit()


@pytest.fixture
def login_handler(driver):
    login(driver)

    return driver
