from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach',True)

driver = webdriver.Chrome(options=opts)

driver.get('https://supertails.com/')
driver.maximize_window()

action = ActionChains(driver)
wait = WebDriverWait(driver,10)
sleep(3)
action.send_keys(Keys.PAGE_DOWN).perform()
sleep(3)
action.send_keys(Keys.PAGE_UP).perform()
sleep(3)
