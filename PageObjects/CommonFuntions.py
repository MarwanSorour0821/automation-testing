from selenium import webdriver
from seleniumpagefactory.Pagefactory import PageFactory
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CommonFuntions(PageFactory):

    def __init__(self,driver):
        self.driver = driver

    def waitForPageToLoadAndScrollToElement(self, methodOfFinding, element_to_find):
        element = WebDriverWait(self.driver,10).until(EC.presence_of_element_located(By.methodOfFinding, element_to_find))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)


    