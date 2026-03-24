from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach',True)
driver = webdriver.Chrome(options=opts)
driver.get('https://demo.automationtesting.in/Frames.html')
driver.maximize_window()
sleep(2)

iframe = driver.find_element(By.ID,'singleframe')
driver.switch_to.frame(iframe)

driver.find_element(By.XPATH,'//input[@type="text"]').send_keys('12345')

driver.switch_to.default_content()
driver.find_element(By.XPATH,'//a[text()="Iframe with in an Iframe"]').click()

## nested
iframe_outer = driver.find_element(By.XPATH,'//iframe[@src="MultipleFrames.html"]')
driver.switch_to.frame(iframe_outer)

iframe_inner = driver.find_element(By.XPATH,'//iframe[@src="SingleFrame.html"]')
driver.switch_to.frame(iframe_inner)

driver.find_element(By.XPATH,'//input[@type="text"]').send_keys('12345')

# driver.switch_to.parent()