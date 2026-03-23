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

driver.get('https://www.royalchallengers.com/')
driver.maximize_window()
sleep(3)

vk18 = driver.find_element(By.XPATH,'(//div[@class="field-content"])[11]')

action = ActionChains(driver)

action.scroll_to_element(vk18).perform()

sleep(3)
for i in range(5):
    sleep(1)
    action.send_keys(Keys.PAGE_UP).perform()
