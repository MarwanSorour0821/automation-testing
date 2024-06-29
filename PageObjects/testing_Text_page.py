from selenium import webdriver
from seleniumpagefactory.Pagefactory import PageFactory
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PageObjects.CommonFuntions import CommonFuntions



class text_test_page(CommonFuntions):

    def __init__(self,driver):
        self.driver = driver
    
    locators = {
        "name_field" : ("ID", "userName"),
        "email_field": ("ID", "userEmail"),
        "current_address": ("ID", "currentAddress"),
        "permanent_address": ("ID", "permanentAddress"),
        "submit_button": ("ID", "submit")
    }

    def typeUserNameInTextField(self):
        self.name_field.send_keys("admin")
    
    def typeEmailInTextField(self):
        self.email_field.send_keys("admin@gmail.com")
    
    def typeCurrentAddress(self):
        self.current_address.send_keys("New York, Wall Street")

    def typePermanentAddress(self):
        self.permanent_address.send_keys("Westchester")
    
    def findSubmitButton(self):
        button_location = self.GoToElementByID("submit")
        return button_location

    def clickSubmitButton(self):
        self.submit_button.click()
    