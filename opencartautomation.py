import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

servicee=Service(r'C:\Users\ASHUTOSH\Documents\chromedriver-win64\chromedriver.exe')

driver=webdriver.Chrome(service=servicee)
driver.get('https://demo.opencart.com/')

try:
    driver.find_element(By.XPATH, "//input[@type='text']").send_keys("phone")
    driver.find_element(By.XPATH, "(//button[@type='button'])[1]").click()
    driver.find_element(By.XPATH, "(//img[@alt='iPhone'])[1]").click()
    driver.find_element(By.XPATH, "//button[text()='Add to Cart']").click()
    time.sleep(5)
    driver.find_element(By.XPATH, "//button[@data-bs-toggle='dropdown']").click()

    driver.find_element(By.XPATH, "//strong[normalize-space()='Checkout']").click()
    driver.find_element(By.XPATH, "//button[@formaction='https://demo.opencart.com/en-gb?route=checkout/cart.remove']").click()









except Exception as e:
    print("error is", e)
time.sleep(3)

driver.close()