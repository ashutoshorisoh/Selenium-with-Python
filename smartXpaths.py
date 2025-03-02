import time
from itertools import count

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import visibility_of_element_located
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.implicitly_wait(3)



driver.get('https://rahulshettyacademy.com/upload-download-test/index.html')

papaya_name= driver.find_element(By.XPATH, "//div[@id='row-2']/div[2]/div")
papaya_price = driver.find_element(By.XPATH, "//div[@id='row-2']/div[4]/div")
print(f"{papaya_name.text}'s price is {papaya_price.text}")




time.sleep(3)
driver.close()