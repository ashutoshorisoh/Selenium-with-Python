import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service  # ✅ Correct import for Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

service_obj = Service(r'C:\Users\ASHUTOSH\Documents\chromedriver-win64\chromedriver.exe')  # Ensure path points to chromedriver.exe
driver = webdriver.Chrome(service=service_obj)
driver.get('https://rahulshettyacademy.com/angularpractice/')
driver.find_element(By.NAME, "name").send_keys("Ashutosh Thakur")
driver.find_element(By.NAME, "email").send_keys("ashuto@gmail.com")
driver.find_element(By.ID, "exampleInputPassword1").send_keys("1234")
driver.find_element(By.ID, "exampleCheck1").click()
select_gender=driver.find_element(By.ID, "exampleFormControlSelect1")
select=Select(select_gender)
select.select_by_visible_text("Female")

driver.find_element(By.XPATH, "//label[@for='inlineRadio1']").click()
driver.find_element(By.NAME,"bday").send_keys("20-02-2002")
driver.find_element(By.XPATH, "//input[@value='Submit']").click()
message=driver.find_element(By.CLASS_NAME, "alert-success").text
print(message.replace('×', "").strip())  # Correct replacement for '×'
assert "Success" in message




time.sleep(10)
driver.quit()