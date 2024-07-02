import pytest
import selenium.webdriver
from selenium import webdriver


@pytest.fixture(scope="session")
def driver():
    driver = webdriver.Chrome()
    
    driver.implicitly_wait(10)
    
    yield driver
    
    driver.quit()