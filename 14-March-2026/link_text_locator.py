
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach',True)
opts.add_argument('--headless')

driver = webdriver.Chrome(options=opts)
driver.get('https://testautomationpractice.blogspot.com/')
sleep(5)

## to use this the element must be a link and it must have a text then only you can use this type of locators
driver.find_element(By.LINK_TEXT,"Udemy Courses")
driver.find_element(By.PARTIAL_LINK_TEXT,"Udemy")

driver.find_element(By.XPATH,'//td[text()="Learn Java"]/following-sibling::td[3]')
driver.find_element(By.XPATH,'//td[text()="Amod"]/ancestor::table/descendant::td[3]')
driver.find_elements(By.XPATH,'//td[text()="300"]/preceding-sibling::td[3]')
name = driver.find_elements(By.XPATH,'//table[@id="taskTable"]/descendant::tbody/descendant::tr/td[1]')
print(len(name))