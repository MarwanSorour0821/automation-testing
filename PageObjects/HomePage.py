from selenium import webdriver
from seleniumpagefactory.Pagefactory import PageFactory
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PageObjects.CommonFuntions import CommonFuntions

class HomePage(CommonFuntions):
    def __init__(self,driver):
        super().__init__(driver)
    
    
    locators = {
        "element_button" : ("CLASS_NAME", "card-up")
    }

    def find_the_element_in_home(self, element_class_name):
        element = self.waitForPageToLoadAndScrollToElement(element_class_name)
        return element
        
    def click_element_button(self):
        self.element_button.click()
        
        


