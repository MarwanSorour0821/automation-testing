from selenium import webdriver
from PageObjects.HomePage import homePage
from PageObjects.CommonFuntions import CommonFuntions
from PageObjects.ChoosePage import chooseTheTab
from PageObjects.testing_Text_page import text_test_page
from selenium.webdriver.common.by import By


#Pages to test
def test_home_page(driver):
    element_to_find = "card-up"
    driver.get("https://demoqa.com")
    home_page = homePage(driver)
    home_page.find_the_element_in_home(element_to_find)
    home_page.click_element_button()

   
def test_choose_element_page(driver):
    choose_element = chooseTheTab(driver)
    choose_element.chooseElementTab()


def test_typingInputs(driver):
    #INPUTS 
    name = "John Doe"
    email = "john@gmail.com"
    current_address = "New york"
    permanent_address = "Cairo"
    
    #initialise
    textPage = text_test_page(driver)
    
    #typing the inputs 
    textPage.typeUserNameInTextField(name)
    textPage.typeEmailInTextField(email)
    textPage.typeCurrentAddress(current_address)
    textPage.typePermanentAddress(permanent_address)
    textPage.clickSubmitButton()

    #verify the inputs against the outputs
    textPage.verifySubmittedName(name)
    textPage.verifySubmittedEmail(email)
    textPage.verifyCurrentAddress(current_address)
    textPage.verifyPermanentAddress(permanent_address)

