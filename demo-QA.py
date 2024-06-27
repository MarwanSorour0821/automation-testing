import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://demoqa.com/")

#wait for content to load
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "home-content")))

#element I want to interact with which is the forms button
search_for_element = driver.find_element(By.CLASS_NAME, "card-up")

# Scroll the element into view
driver.execute_script("arguments[0].scrollIntoView(true);", search_for_element)

#action for the forms button
search_for_element.click()

search_for_element_text = driver.find_element(By.ID, "item-0")
# driver.execute_script("arguments[0].scrollIntoView(true);", search_for_element_text)
search_for_element_text.click()

#search for user name text box
search_for_firstName = driver.find_element(By.ID, "userName")

#type the username
search_for_firstName.send_keys("admin")


#search for user email
search_for_email = driver.find_element(By.ID, "userEmail")

#type email
search_for_email.send_keys("admin@gmail")


#search for address input text box
search_for_address = driver.find_element(By.ID, "currentAddress").send_keys("Wall Street, New York")
search_for_permanent_address = driver.find_element(By.ID, "permanentAddress").send_keys("New York, Manhattan")

#Submit form
search_for_submit_button = driver.find_element(By.ID, "submit")

driver.execute_script("arguments[0].scrollIntoView(true);", search_for_submit_button)

search_for_submit_button.click()

driver.close()