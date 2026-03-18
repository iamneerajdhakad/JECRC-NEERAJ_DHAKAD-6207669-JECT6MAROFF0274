
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach',True)
driver = webdriver.Chrome(options=opts)

driver.get('https://www.lenskart.com/')
driver.maximize_window()
sleep(5)

eyeglass = driver.find_element(By.ID,'lrd1')
# print(eyeglass.text)

assert 'GLASSES' in eyeglass.text, 'could not find the element'
print('successful assert 1')

brand_name = driver.find_element(By.XPATH,'//h3[@class="sc-5c474d1e-0 gcOylD"]')

assert 'Top' in brand_name.text, 'could not find the element'
print('successful assert 2')

driver.get('https://www.lenskart.com/lenskart-studio-lk-s18862-c1-sunglasses.html')

sleep(5)
temp = driver.find_element(By.XPATH,'//p[@title="Enter pincode"]')
sleep(5)
temp.click()
# check_btn = driver.find_element(By.XPATH,'//div[@class="sc-a3b31f26-14 fDEfLM"]')
# assert check_btn.is_enabled(), 'check box is not enabled'

sleep(10)
driver.quit()
