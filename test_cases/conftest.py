import pytest
from selenium import webdriver


@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    return driver
