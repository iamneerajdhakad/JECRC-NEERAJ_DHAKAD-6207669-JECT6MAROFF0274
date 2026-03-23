from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach',True)

driver = webdriver.Chrome(options=opts)

driver.get('https://www.myntra.com/')
driver.maximize_window()
sleep(3)

action = ActionChains(driver)

sleep(2)
women = driver.find_element(By.XPATH,'//a[text()="Women"]')

action.move_to_element(women).perform()