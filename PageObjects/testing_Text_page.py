from selenium import webdriver
from seleniumpagefactory.Pagefactory import PageFactory
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PageObjects.CommonFuntions import CommonFuntions

class text_test_page(CommonFuntions):

    def __init__(self,driver):
        super().__init__(driver)
    
    locators = {
        #Text form Inputs
        "name_field" : (By.ID, "userName"),
        "email_field": (By.ID, "userEmail"),
        "current_address": (By.ID, "currentAddress"),
        "permanent_address": (By.ID, "permanentAddress"),
        "submit_button": (By.ID, "submit"),

        #expected text form outputs
        "submittedName": (By.ID, "name"),
        "submittedEmail": (By.ID, "email"),

        #THESE HAD TO BE XPATH BECAUSE THEY HAD THE SAME ID AS THE INPUT TEXT FIELD
        "submittedCurrentAddress": (By.XPATH, "//*[@class='border col-md-12 col-sm-12']/*[@id='currentAddress']"),
        "submittedPermanentAddress": (By.XPATH, "//*[@class='border col-md-12 col-sm-12']/*[@id='permanentAddress']")
    }

    #ACTION FUNCTIONS
    def typeUserNameInTextField(self, user_name):
        user_name_field = self.driver.find_element(*self.locators["name_field"])
        #empty text field before inputting new text
        user_name_field.clear()
        user_name_field.send_keys(user_name)

    def typeEmailInTextField(self, email):
        email_field = self.driver.find_element(*self.locators["email_field"])
        email_field.clear()
        email_field.send_keys(email)

    def typeCurrentAddress(self, address):
        current_address_field = self.driver.find_element(*self.locators["current_address"])
        current_address_field.clear()
        current_address_field.send_keys(address)

    def typePermanentAddress(self, address):
        permanent_address_field = self.driver.find_element(*self.locators["permanent_address"])
        permanent_address_field.clear()
        permanent_address_field.send_keys(address)

    def findSubmitButton(self):
        return self.driver.find_element(*self.locators["submit_button"])

    def clickSubmitButton(self):
        submit_button = self.findSubmitButton()
        self.driver.execute_script("arguments[0].scrollIntoView();", submit_button)
        submit_button.click()
    
    #VERIFICATION FUNCTIONS 
    #check if the name inputted is the same in the name outputted by accessing the text inside the element by ID
    def verifySubmittedName(self, expectedName):
        element = self.driver.find_element(*self.locators["submittedName"])
        assert expectedName in element.text
    
    def verifySubmittedEmail(self, expectedEmail):
        element = self.driver.find_element(*self.locators["submittedEmail"])
        assert expectedEmail in element.text
    
    def verifyCurrentAddress(self, expectedCurrentAddress):
        element = self.driver.find_element(*self.locators["submittedCurrentAddress"])
        assert expectedCurrentAddress in element.text
    
    def verifyPermanentAddress(self, expectedPermanentAddress):
        element = self.driver.find_element(*self.locators["submittedPermanentAddress"])
        assert expectedPermanentAddress in element.text
    