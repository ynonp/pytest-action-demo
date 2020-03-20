from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import pytest

@pytest.fixture(scope='session')
def browser(request):
    options = Options()
    options.headless = True
    driver = webdriver.Firefox(options=options) 
    driver.implicitly_wait(5)
    yield driver
    driver.close()
