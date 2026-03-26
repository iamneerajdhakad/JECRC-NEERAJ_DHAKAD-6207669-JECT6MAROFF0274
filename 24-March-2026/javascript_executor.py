
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
driver.execute_script('window.scrollTo(0,document.body.scrollHeight);')
sleep(2)
driver.execute_script('window.scrollTo(0,0);')
sleep(2)
driver.execute_script('window.scrollBy(0,500);')
sleep(2)
driver.execute_script('window.scrollBy(0,-200);')
sleep(5)
element = driver.find_element(By.XPATH,'(//div[@class="WuRgKB eMU5i5 o5UlW_ hL1e7w"])[2]')
driver.execute_script('arguments[0].scrollIntoView();',element)
sleep(5)
driver.execute_script("arguments[0].style.border='3px solid red'", element)
driver.execute_script("arguments[0].remove();", element)
# driver.execute_script('arguments[0].click();',element)

