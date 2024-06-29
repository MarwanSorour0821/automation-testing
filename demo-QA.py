import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PageObjects.HomePage import HomePage
from PageObjects.CommonFuntions import CommonFuntions





#Go to browser
driver = webdriver.Chrome()
driver.get("https://demoqa.com/")

print("going in function")
def test_home_page():
    print("inside function")
    home_page = HomePage(driver)
    common = CommonFuntions(driver)
    element_to_find = "card-up"
    #action
    common.waitForPageToLoadAndScrollToElement(element_to_find)
    # home_page.waitForPageToLoadAndScrollToElement("card-up")
    #homePageElement = 
    home_page.find_the_element_in_home(element_to_find)
    home_page.click_element_button()

    #assertion print
    print("Home Page test passed")


test_home_page()

# def test_find_element_tab():
#     pass








# search_for_element_text = driver.find_element(By.ID, "item-0")
# # driver.execute_script("arguments[0].scrollIntoView(true);", search_for_element_text)
# search_for_element_text.click()

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