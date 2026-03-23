from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
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

dog = wait.until(EC.visibility_of_element_located((By.XPATH,'//div[@data-ganame="Breed 1"]')))
action.scroll_to_element(dog).perform()

action.scroll_by_amount(0,-500).perform()
action.scroll_to_element(dog).perform()

action.context_click(dog).perform()
action.click(dog).perform()

