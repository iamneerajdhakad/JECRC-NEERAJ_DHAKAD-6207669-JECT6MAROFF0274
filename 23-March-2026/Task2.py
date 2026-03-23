from os import access
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

driver.get('https://www.myntra.com/')
driver.maximize_window()
sleep(3)

wait = WebDriverWait(driver,10)
action = ActionChains(driver)

sleep(1)
Men = wait.until(EC.visibility_of_element_located((By.XPATH,'(//a[text()="Men"])[1]')))
action.move_to_element(Men).perform()

sleep(1)
wait.until(EC.visibility_of_element_located((By.XPATH,'//a[text()="T-Shirts"]'))).click()

sleep(1)
row_ele = wait.until(EC.presence_of_element_located((By.XPATH,'//ul[@class="results-base"]/li[17]')))

sleep(1)
action.scroll_to_element(row_ele).perform()