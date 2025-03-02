import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import visibility_of_element_located
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.implicitly_wait(3)



driver.get('https://rahulshettyacademy.com/upload-download-test/index.html') 


download_btn = driver.find_element(By.CSS_SELECTOR, "#downloadButton")
download_btn.click()


upload_btn= driver.find_element(By.CSS_SELECTOR, "input[type='file']")
upload_btn.send_keys(r"C:\Users\ASHUTOSH\Downloads\download.xlsx")

wait = WebDriverWait(driver, 10)
locator_toast= (By.XPATH, "//div[contains(text(),'Updated Excel Data Successfully.')]")
wait.until(visibility_of_element_located(locator_toast))











time.sleep(2)

driver.close()
