## Task 2
from time import sleep

### Alerts

# 1. navigate to the url: `https://demoqa.com/alerts`
# 2. work on all the 4 alerts one after the other
# 3. validate the result appearing, eg: for `ok` you should assert with it the result shown

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach',True)

driver = webdriver.Chrome(options=opts)
driver.get('https://demoqa.com/alerts')
driver.maximize_window()

wait = WebDriverWait(driver,6)

driver.find_element(By.ID,'alertButton').click()
alert_1 = wait.until(EC.alert_is_present())
alert_1.accept()

driver.find_element(By.ID,'timerAlertButton').click()
alert_2 = wait.until(EC.alert_is_present())
alert_2.accept()

driver.find_element(By.ID,'confirmButton').click()
alert_3 = wait.until(EC.alert_is_present())
alert_3.dismiss()

selected = driver.find_element(By.ID,'confirmResult').text

assert 'Ok' in selected or 'Cancel' in selected , "Error"

driver.find_element(By.ID,'promtButton').click()

alert_4 = wait.until(EC.alert_is_present())
alert_4.send_keys('qwerty')
alert_4.accept()

assert 'qwerty' in driver.find_element(By.ID,'promptResult').text, "Error"
