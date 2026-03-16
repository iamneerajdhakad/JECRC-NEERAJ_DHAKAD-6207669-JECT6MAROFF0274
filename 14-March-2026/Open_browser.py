from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()

driver.get('https://www.amazon.in/')
sleep(2)
driver.get('https://www.cricbuzz.com/')
sleep(2)
driver.get('https://www.myntra.com/')
sleep(2)
driver.quit()
