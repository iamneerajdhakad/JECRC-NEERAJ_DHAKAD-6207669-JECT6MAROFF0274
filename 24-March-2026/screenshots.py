import os
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

folder = os.path.join(os.getcwd(),'screenshots')
os.makedirs(folder,exist_ok=True)

opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach',True)
driver = webdriver.Chrome(options=opts)

driver.get('https://www.pinterest.com/')
driver.maximize_window()

sleep(2)

driver.save_screenshot(f'{folder}/full_page.png') ### full screenshot
action = ActionChains(driver)

element = driver.find_element(By.XPATH,'(//div[@class="ADXRXN AsRsEE"])[3]/descendant::img')
action.scroll_to_element(element).perform()
element.screenshot(f'{folder}/element.png')

element_2 = driver.find_element(By.XPATH,'//img[contains(@alt,"bright lip")]')
action.scroll_to_element(element_2).perform()
element_2.screenshot(f'{folder}/element_2.png')