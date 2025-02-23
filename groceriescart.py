import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

# Setup ChromeDriver
servicee = Service(r'C:\Users\ASHUTOSH\Documents\chromedriver-win64\chromedriver.exe')
driver = webdriver.Chrome(service=servicee)

driver.implicitly_wait(3)  # Implicit wait
wait=WebDriverWait(driver, 15)
driver.get('https://rahulshettyacademy.com/seleniumPractise/#/')

driver.find_element(By.CSS_SELECTOR, ".search-keyword").send_keys("berry")
driver.find_element(By.CSS_SELECTOR, ".search-button").click()

time.sleep(2)  # Allow time for products to load

result= driver.find_elements(By.XPATH, "//div[@class='products']/div")

for product in result:
    add_btn= product.find_element(By.XPATH, "div/button")
    add_btn.click() #important

cartPreview= driver.find_element(By.CSS_SELECTOR, ".cart-icon")
cartPreview.click()

checkoutBtn= driver.find_element(By.CSS_SELECTOR, ".action-block")
checkoutBtn.click()

promocode= driver.find_element(By.CSS_SELECTOR, ".promoCode")
promocode.send_keys("rahulshettyacademy")

promoBtn= driver.find_element(By.CSS_SELECTOR, ".promoBtn")
promoBtn.click()
time.sleep(5)

promoStatus= driver.find_element(By.CSS_SELECTOR, ".promoInfo")

assert promoStatus.text == "Code applied ..!"

beforeAmount= int(driver.find_element(By.CSS_SELECTOR, ".totAmt").text)
afterAmount= int(driver.find_element(By.CSS_SELECTOR, ".discountAmt").text)

assert afterAmount<=beforeAmount, "discount not applied"

placeOrder = driver.find_element(By.XPATH, "//button[text()='Place Order']")
placeOrder.click()

Country= Select(driver.find_element(By.XPATH, "//div[@class='wrapperTwo']//div//select"))
Country.select_by_visible_text("India")

agree= driver.find_element(By.CSS_SELECTOR, ".chkAgree")
agree.click()

proceed=driver.find_element(By.XPATH, "//button[normalize-space()='Proceed']")
proceed.click()





time.sleep(3)
driver.quit()
