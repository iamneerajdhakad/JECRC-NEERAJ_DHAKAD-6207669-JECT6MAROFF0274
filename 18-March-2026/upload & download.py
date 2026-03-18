
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach',True)
driver = webdriver.Chrome(options=opts)

driver.get('https://the-internet.herokuapp.com/')
driver.maximize_window()
sleep(3)

download_btn = driver.find_element(By.XPATH,'//a[text()="File Download"]')
download_btn.click()
sleep(2)

image = driver.find_element(By.XPATH,'//a[text()="file1.txt"]')
image.click()
sleep(5)

driver.back()
sleep(2)

upload_site_btn = driver.find_element(By.XPATH,'//a[text()="File Upload"]')
upload_site_btn.click()
sleep(2)

choose_file_btn = driver.find_element(By.XPATH,'//input[@id="file-upload"]')
choose_file_btn.send_keys(r'C:\Users\neera\Downloads\Upload_Test.txt')
sleep(5)

upload_btn = driver.find_element(By.ID,'file-submit')
upload_btn.click()

sleep(3)
driver.quit()