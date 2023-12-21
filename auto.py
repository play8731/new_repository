from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time

options=Options()
options.chrome_executable_path= r"C:\Users\play8\OneDrive\Desktop\chromedriver_win32\chromedriver.exe"

driver=webdriver.Chrome(options=options)
driver.get("https://24h.pchome.com.tw/")

usernameInput=driver.find_element(By.CLASS_NAME, 'l-header__siteSearchInput')
usernameInput.send_keys("Whoscall")

usernameInput.send_keys(Keys.ENTER)

product = driver.find_element(By.CLASS_NAME, 'prod_name')
product.send_keys(Keys.click)

#element = driver.find_element_by_id("")
#driver.execute_script("arguments[0].scrollIntoView(true);", element)
#driver.save_screenshot("screenshot.png")

time.sleep(3)
driver.close()
