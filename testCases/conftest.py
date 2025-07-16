import pytest
from selenium import webdriver

def pytest_addoption(parser):
    parser.addoption("--browser",default="chrome")

@pytest.fixture
def setup(browser):
    if browser == "chrome":
        driver=webdriver.Chrome()
        driver.maximize_window()
        return driver
    else:
        print("Niranjan")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")