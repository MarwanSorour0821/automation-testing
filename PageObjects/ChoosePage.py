from selenium import webdriver
from seleniumpagefactory.Pagefactory import PageFactory
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PageObjects.CommonFuntions import CommonFuntions


class chooseTheTab(PageFactory):

    def __init__(self,driver):
        self.driver = driver
    
    locators = {
        "text_button" : ("ID", "item-0")
    }
    
    def chooseElementTab(self):
        self.text_button.click()

