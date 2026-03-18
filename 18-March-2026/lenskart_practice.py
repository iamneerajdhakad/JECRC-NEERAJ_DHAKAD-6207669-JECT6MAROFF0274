from time import sleep

from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach',True)

driver = webdriver.Chrome(options=opts)

driver.get('https://www.lenskart.com/')
driver.maximize_window()
sleep(3)

search_field = driver.find_element(By.XPATH,'//input[@class="aa-Input"]')
search_field.send_keys('square frame',Keys.ENTER)
sleep(3)

drop_down_btn = driver.find_element(By.XPATH,'//select[@id="sortByDropdown"]')
drop_down = Select(drop_down_btn)
drop_down.select_by_value('low_price')

sleep(3)
first_row = driver.find_element(By.XPATH,'//div[@class="sc-bf32d8a7-0 gOVKHN"]/descendant::div/p')

print(f'First Image Text: {first_row.text}')

driver.quit()
