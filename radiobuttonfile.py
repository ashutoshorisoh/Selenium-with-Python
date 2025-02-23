import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


servicee=Service(r'C:\Users\ASHUTOSH\Documents\chromedriver-win64\chromedriver.exe')

driver=webdriver.Chrome(service=servicee)
driver.get('https://rahulshettyacademy.com/AutomationPractice/')

radio = driver.find_element(By.CSS_SELECTOR, "input[value='radio1']")
radio.click()

assert radio.is_selected(), "radio is not selected"

type_country= driver.find_element(By.CSS_SELECTOR, "input[placeholder='Type to Select Countries']")
type_country.send_keys("india")
time.sleep(1)

options = driver.find_elements(By.CLASS_NAME, "ui-menu-item-wrapper")  # Gets all dropdown options

for option in options:
    if option.text == "India":
        option.click()
        break  # Stop after selecting the correct option

# Verify selection
assert type_country.get_attribute("value") == "India", "Selection failed!"


dropDown = Select(driver.find_element(By.ID, "dropdown-class-example"))
dropDown.select_by_visible_text("Option2")

assert dropDown.first_selected_option.text=="Option2", "selection failed"

checkBoxes = driver.find_elements(By.CSS_SELECTOR, "div#checkbox-example input[type='checkbox']")

for op in checkBoxes:
    if op.get_attribute("id")=="checkBoxOption1":
        op.click()
        assert op.is_selected(), "failed"
        break




time.sleep(3)

driver.close()