from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach',True)
driver = webdriver.Chrome(options=opts)
driver.get('http://the-internet.herokuapp.com/javascript_alerts')
driver.maximize_window()
sleep(2)

wait = WebDriverWait(driver,10)

driver.find_element(By.XPATH,'//button').click()
alert = driver.switch_to.alert
alert.accept()
sleep(2)

driver.find_element(By.XPATH,'(//button)[2]').click()
alert = driver.switch_to.alert
alert.dismiss()
sleep(2)

driver.find_element(By.XPATH,'(//button)[3]').click()
alert = driver.switch_to.alert
alert.send_keys('Hello Selenium')
sleep(2)
alert.accept()
sleep(2)

driver.find_element(By.XPATH,'//button').click()
alert = wait.until(EC.alert_is_present())
sleep(2)
alert.accept()
