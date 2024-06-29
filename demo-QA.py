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
    typingElement.clickSubmitButton()

#Tests for pages
test_home_page()
test_choose_element_page()
test_typingInputs()

print("DONE")







# #search for user name text box
# search_for_firstName = driver.find_element(By.ID, "userName")

# #type the username
# search_for_firstName.send_keys("admin")


# #search for user email
# search_for_email = driver.find_element(By.ID, "userEmail")

# #type email
# search_for_email.send_keys("admin@gmail.com")


# #search for address input text box
# search_for_address = driver.find_element(By.ID, "currentAddress").send_keys("Wall Street, New York")
# search_for_permanent_address = driver.find_element(By.ID, "permanentAddress").send_keys("New York, Manhattan")

# #Submit form
# search_for_submit_button = driver.find_element(By.ID, "submit")

# driver.execute_script("arguments[0].scrollIntoView(true);", search_for_submit_button)

# search_for_submit_button.click()

# driver.close()