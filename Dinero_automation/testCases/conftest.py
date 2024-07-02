from datetime import datetime
import pytest
from selenium import webdriver
import os

@pytest.fixture()
def setup(browser):
    if browser == 'edge':
        driver = webdriver.Edge()
        print("Launching Edge browser.........")
    elif browser == 'firefox':
        driver = webdriver.Firefox()
        print("Launching Firefox browser.........")
    else:
        driver = webdriver.Chrome()
        print("Launching Chrome browser.........")
    return driver

def pytest_addoption(parser):    # This will get the value from CLI /hooks
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):  # This will return the Browser value to setup method
    return request.config.getoption("--browser")


########### pytest HTML Report ################

# It is hook for Adding Environment info to HTML Report
@pytest.hookimpl()
def pytest_configure(config):
    config._metadata['Project Name'] = 'Dinero'
    config._metadata['Tester'] = 'Karunakar'

# It is hook for delete/Modify Environment info to HTML Report
@pytest.hookimpl(optionalhook=True)
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)

#Specifying report folder location and save report with timestamp
@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    reports_path = '/home/karunakar/PycharmProjects/Dinero_UI_Automation/reports/'
    config.option.htmlpath = reports_path + datetime.now().strftime("%d-%m-%Y %H-%M-%S")+".html"




