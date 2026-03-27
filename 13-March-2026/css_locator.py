from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach',True)
opts.add_argument('--headless')
driver = webdriver.Chrome(options=opts)
driver.get('https://testautomationpractice.blogspot.com/')
driver.maximize_window()
sleep(1)

name = driver.find_element(By.CSS_SELECTOR,'select[id="animals"]')
email = driver.find_element(By.CSS_SELECTOR,'input[id="email"]')
x = driver.find_elements(By.CSS_SELECTOR,'input[class="form-control"][id="email"]')
y = driver.find_elements(By.CSS_SELECTOR,'input[class="form-control"]')
phone = driver.find_element(By.CSS_SELECTOR,'input[id="phone"]')
div = driver.find_element(By.CSS_SELECTOR,'div[id="main"]')
a = driver.find_element(By.CSS_SELECTOR,'a[ href*="testautomationpractice"]')
b = driver.find_element(By.CSS_SELECTOR,'a[ href^="http"]')
c = driver.find_element(By.CSS_SELECTOR,'a[ href$=".com"]')
d = driver.find_element(By.CSS_SELECTOR,'div[class="widget-content"] a[href$=".com"]')
print(len(x))
print(len(y))
driver.quit()