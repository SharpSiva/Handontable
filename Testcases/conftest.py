from selenium import webdriver
driver=webdriver.Chrome(executable_path='C:/Users/aasiva/Downloads/chromedriver_win92/chromedriver.exe')
import pytest

@pytest.fixture()
def setup(browser):
    if browser=='chrome':
        driver=webdriver.Chrome()
        print("Launching chrome browser........")
    elif browser=='firefox':
        driver=webdriver.Firefox()
        print("Launching Firefox browser........")
    else:
        driver=webdriver.Ie()
        print("Launching Ie browser........")
    return driver

def pytest_addoption(parser):   #this will get value from hooks
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):     #this will return browser value to setup method
    return request.config.getoption("--browser")

#Adding enviroment info to HTML Report
def pytest_configure(config):
    config._metadata['Project Name'] = "Handontable"
    config._metadata['Module']="User"
    config._metadata['Tester']='Ben'

@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_Home",None)
    metadata.pop("Plugins",None)