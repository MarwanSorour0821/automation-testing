from selenium import webdriver
from seleniumpagefactory.Pagefactory import PageFactory
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PageObjects.CommonFuntions import waitForPageToLoadAndScrollToElement

class HomePage(PageFactory):
    def __init__(self,driver):
        self.driver = driver
    



    locators = {
        "element_button" : ("CLASS_NAME", "card-up")
    }

    #wait for the lement 
    waitForPageToLoadAndScrollToElement("CLASS_NAME","card-up")

    def find_the_element_in_home(self,methodOfFinding, element):
        self.element.find_element(By.methodOfFinding, element)
        
    def click_element_button(self, element):
        self.element.click()


