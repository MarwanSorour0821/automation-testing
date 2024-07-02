from selenium import webdriver
from selenium.webdriver.common.by import By
from PageObjects.CommonFuntions import CommonFuntions

class chooseTheTab(CommonFuntions):

    def __init__(self,driver):
        super().__init__(driver)
    
    locators = {
        "text_button" : (By.ID, "item-0")
    }
    
    def chooseElementTab(self):
        #scroll to element and find it and click the element
        element_button = self.driver.find_element(*self.locators["text_button"])
        self.driver.execute_script("arguments[0].scrollIntoView();", element_button)
        element_button.click()

