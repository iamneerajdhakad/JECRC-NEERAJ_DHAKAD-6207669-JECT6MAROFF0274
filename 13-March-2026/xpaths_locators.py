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

driver.find_element(By.XPATH,'//input[@placeholder="Enter Name"]')
driver.find_element(By.XPATH,'//style[@type="text/css"]')
driver.find_element(By.XPATH,'//meta[@content="blogspot.com"]')
driver.find_element(By.XPATH,'//script[@type="text/javascript"]')
driver.find_element(By.XPATH,'//div[@data-version="1"]')
driver.find_element(By.XPATH,'//a[text()="Home"]')
driver.find_element(By.XPATH,'//a[text()="Udemy Courses"]')
driver.find_element(By.XPATH,'//label[text()="Name:"]')
driver.find_element(By.XPATH,'//h2[text()="Dynamic Button"]')
driver.find_element(By.XPATH,'//h2[contains(text(),"Dynamic Button")]')
driver.find_element(By.XPATH,'//option[contains(text(),"Blue")]')

driver.quit()