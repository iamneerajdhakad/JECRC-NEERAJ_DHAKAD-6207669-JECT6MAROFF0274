from time import sleep

from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By

opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach',True)

driver = webdriver.Chrome(options=opts)

driver.get('https://testautomationpractice.blogspot.com/')
driver.maximize_window()
sleep(3)

drop_down_btn = driver.find_element(By.ID,'country')

drop_down = Select(drop_down_btn)
sleep(3)
drop_down.select_by_value('usa')
sleep(3)
drop_down.select_by_index(4)
sleep(3)
drop_down.select_by_visible_text('India')
sleep(3)
