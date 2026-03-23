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

driver.get(r'C:\Python\Testing\Selenium_Framework\23-March-2026\html_page.html')
driver.maximize_window()

wait = WebDriverWait(driver,10)
action = ActionChains(driver)

present_add = wait.until(EC.visibility_of_element_located((By.ID,'presentAddress')))
permanent_add = wait.until(EC.visibility_of_element_located((By.ID,'permanentAddress')))

present_add.send_keys('Kumbha Marg Pratap Nagar')
present_add.click()

action.key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).perform()
sleep(2)

action.key_down(Keys.CONTROL).send_keys('c').key_up(Keys.CONTROL).perform()
sleep(2)

permanent_add.click()

action.key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).perform()



