from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.chrome.service import Service
import pytest


@pytest.fixture()
def setup(browser):
    global driver
    if browser == 'Chrome':
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        print("................Launching Chrome Browser...........")
    elif browser == 'Edge':
        print("............Launching Edge Browser..............")
        driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))
    else:
        driver = webdriver.Ie()
    return driver


def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")


# Generate HTML Report

# Hook for Adding information into HTML Report

def pytest_configure(config):
    config._metadata['Project Name'] = 'Test Framework by Pranto'
    config._metadata['Module Name'] = 'Login Module'
    config._metadata['Tester'] = 'Md Maksud Hossain Pranto'

# Hook for Delete / Modify info in HTML Report


@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)
    metadata.pop("Packages", None)



