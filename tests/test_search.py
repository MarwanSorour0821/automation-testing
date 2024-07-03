from selenium import webdriver
from PageObjects.HomePage import homePage
from PageObjects.CommonFuntions import CommonFuntions
from PageObjects.ChoosePage import chooseTheTab
from PageObjects.testing_Text_page import text_test_page
from PageObjects.reader import readCSVFile
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

    #READ CSV FILE
    test_name_data = readCSVFile('data/inputTextInformation.csv')
    
    #initialise
    textPage = text_test_page(driver)
    
    for row in test_name_data:
        #TYPING INPUTS
        textPage.typeUserNameInTextField(row['input_name'])
        textPage.typeEmailInTextField(row['input_email'])
        textPage.typeCurrentAddress(row['inputCurrentAddress'])
        textPage.typePermanentAddress(row['inputPermanentAddress'])
        textPage.clickSubmitButton()

        #TESTING INPUTS AGAINST OUTPUTS
        textPage.verifySubmittedName(row['expected_name_output'])
        textPage.verifySubmittedEmail(row['expected_email_output'])
        textPage.verifyCurrentAddress(row['expectedCurrentAddress'])
        textPage.verifyPermanentAddress(row['inputPermanentAddress'])
