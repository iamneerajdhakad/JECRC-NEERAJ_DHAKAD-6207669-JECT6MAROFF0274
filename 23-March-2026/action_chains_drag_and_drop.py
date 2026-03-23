
'''
action chains: it basically used for all the action which can be done using mouse & keyboard actions
eg. drag and drop, copy paste,
'''
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach',True)

driver = webdriver.Chrome(options=opts)

driver.get('https://the-internet.herokuapp.com/drag_and_drop')
driver.maximize_window()
sleep(3)

action = ActionChains(driver)

origin_ele = driver.find_element(By.ID,'column-a')
target_ele = driver.find_element(By.ID,'column-b')

action.drag_and_drop(origin_ele,target_ele).perform()

driver.get('https://www.myntra.com/')
sleep(2)
women = driver.find_element(By.XPATH,'//a[text()="Women"]')

action.move_to_element(women).perform()
