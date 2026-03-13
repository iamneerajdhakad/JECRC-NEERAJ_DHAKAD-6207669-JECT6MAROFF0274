from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach',True)
opts.add_argument('--headless')
driver = webdriver.Chrome(options=opts)
driver.get('https://testautomationpractice.blogspot.com/')
driver.maximize_window()
sleep(1)

## using ID
name = driver.find_element(By.ID,'name')
phone_no = driver.find_element(By.ID,'phone')
# print(name)

## using name
nav_bar = driver.find_element(By.NAME,'Navbar')
radio_btn = driver.find_elements(By.CLASS_NAME,'form-heck-label')
inp = driver.find_elements(By.TAG_NAME,'input')
print(name)
print(phone_no)
print(nav_bar)
print(len(radio_btn))
print(len(inp))
driver.quit()