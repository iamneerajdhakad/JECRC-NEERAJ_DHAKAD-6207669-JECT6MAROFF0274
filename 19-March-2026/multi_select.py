from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach',True)

driver = webdriver.Chrome(options=opts)
driver.get('https://testautomationpractice.blogspot.com/')
driver.maximize_window()

multi_drop = driver.find_element(By.ID,'colors')
select = Select(multi_drop)

if select.is_multiple:
    select.select_by_value('yellow')
    select.select_by_index(1)
    select.select_by_value('white')

print([ i.text for i in select.all_selected_options])
sleep(3)

select.deselect_by_index(1)

sleep(3)
print([ i.text for i in select.all_selected_options])
