import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PageObjects.HomePage import HomePage
from PageObjects.CommonFuntions import CommonFuntions
from PageObjects.ChoosePage import chooseTheTab
from PageObjects.testing_Text_page import text_test_page



#Go to browser
driver = webdriver.Chrome()
driver.get("https://demoqa.com/")

#Pages to test
def test_home_page():
    home_page = HomePage(driver)
    common = CommonFuntions(driver)
    element_to_find = "card-up"
    common.waitForPageToLoadAndScrollToElement(element_to_find)
    home_page.find_the_element_in_home(element_to_find)
    home_page.click_element_button()

   
def test_choose_element_page():
    choose_element = chooseTheTab(driver)
    choose_element.chooseElementTab()


def test_typingInputs():
    typingElement = text_test_page(driver)
    typingElement.typeUserNameInTextField()
    typingElement.typeEmailInTextField()
    typingElement.typeCurrentAddress()
    typingElement.typePermanentAddress()
    typingElement.findSubmitButton()
    typingElement.clickSubmitButton()

#Tests for pages --------------------------------------------
test_home_page()
test_choose_element_page()
test_typingInputs()

print("DONE")