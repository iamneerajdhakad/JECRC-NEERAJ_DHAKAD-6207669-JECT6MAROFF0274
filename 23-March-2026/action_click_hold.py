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

driver.get(r'C:\Python\Testing\Selenium_Framework\23-March-2026\html_password.html')
driver.maximize_window()

wait = WebDriverWait(driver,10)
action = ActionChains(driver)
sleep(3)
show_pass = wait.until(EC.visibility_of_element_located((By.ID,'password')))
show_pass.send_keys('1234567890')
action.click_and_hold(wait.until(EC.visibility_of_element_located((By.ID,'eyeBtn')))).perform()

