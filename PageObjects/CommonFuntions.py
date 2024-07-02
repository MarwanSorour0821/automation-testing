from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import selenium
from PageObjects.BaseClass import BaseClass


class CommonFuntions(BaseClass):

    def __init__(self,driver):
        super().__init__()
        self.driver = driver
        
    def waitForPageToLoadAndScrollToElement(self, element_to_find):
        self.driver.implicitly_wait(10)
        


    