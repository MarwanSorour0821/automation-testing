from selenium import webdriver
from seleniumpagefactory.Pagefactory import PageFactory
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CommonFuntions(PageFactory):

    def __init__(self,driver):
        self.driver = driver

    # def waitForPageToLoadAndScrollToElement(self):
    #     WebDriverWait(self.driver,10).until(EC.presence_of_element_located(By.CLASS_NAME, 'card-up'))
    #     self.driver.execute_script("arguments[0].scrollIntoView(true);", 'card-up')
        

    def waitForPageToLoadAndScrollToElement(self, element_to_find):
         # Replace with your actual class name
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, element_to_find))
        )
        # Scroll to the element if needed
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    # search_for_firstName = driver.find_element(By.ID, "userName")


    