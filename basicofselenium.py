import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service  # ✅ Correct import for Chrome

service_obj = Service(r'C:\Users\ASHUTOSH\Documents\chromedriver-win64\chromedriver.exe')  # Ensure path points to chromedriver.exe
driver = webdriver.Chrome(service=service_obj)

driver.get('https://what-textapp.web.app/')
driver.maximize_window()
print(driver.title)
print('current url is ', driver.current_url)




time.sleep(2)

driver.quit()