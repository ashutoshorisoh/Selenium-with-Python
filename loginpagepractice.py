import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


servicee = Service(r'C:\Users\ASHUTOSH\Documents\chromedriver-win64\chromedriver.exe')
driver = webdriver.Chrome(service=servicee)

driver.implicitly_wait(3)
wait=WebDriverWait(driver, 15)

driver.get('https://rahulshettyacademy.com/loginpagePractise/')

redirectButton = driver.find_element(By.CLASS_NAME, "blinkingText")
redirectButton.click()


allWindow= driver.window_handles
driver.switch_to.window(allWindow[1])

getemail= driver.find_element(By.LINK_TEXT, "mentor@rahulshettyacademy.com").text

driver.close()
driver.switch_to.window(allWindow[0])

usernameField= driver.find_element(By.ID, "username")
usernameField.send_keys(getemail)

password=driver.find_element(By.ID, "password")
password.send_keys("learning")

select = Select(driver.find_element(By.TAG_NAME, "select"))
select.select_by_visible_text("Student")

terms= driver.find_element(By.ID, "terms")
terms.click()
assert terms.is_selected(), "Button was not clicked successfully"

signInbtn = driver.find_element(By.ID, "signInBtn")
signInbtn.click()

message = WebDriverWait(driver, 5).until(
    expected_conditions.visibility_of_element_located((By.CLASS_NAME, "alert"))
)

assert message.is_displayed(), "Button click did not trigger expected behavior!"




alert= driver.find_element(By.CLASS_NAME, "alert")

if alert:
    usernameField.clear()
    usernameField.send_keys("rahulshettyacademy")
    select.select_by_visible_text("Student")
    driver.find_element(By.ID, "terms").click()
    driver.find_element(By.ID, "signInBtn").click()

time.sleep(3)
driver.close()