from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach',True)

driver = webdriver.Chrome(options=opts)

driver.get('https://testautomationpractice.blogspot.com/')
driver.maximize_window()
sleep(3)

male = driver.find_element(By.ID,'male')
male.click()

check_box = driver.find_element(By.XPATH,'//label[text()="Days:"]/following-sibling::div/input')
check_box.click()
print(male.is_displayed()) ## if you want to check if it is visible on your UI
print(male.is_enabled()) ## it is used for button to check if it is enabled or not
print(check_box.is_selected()) ## check if the drop
driver.quit()