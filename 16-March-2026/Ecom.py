from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach',True)

driver = webdriver.Chrome(options=opts)

driver.get('https://www.flipkart.com/')
driver.maximize_window()
sleep(2)

cross_btn = driver.find_element(By.XPATH,'//span[@role="button"]')
cross_btn.click()
# search_field = driver.find_element(By.ID,'twotabsearchtextbox')
# search_field.clear()
# search_field.send_keys('Laptop',Keys.ENTER)

# search_buttton = driver.find_element(By.XPATH,'//input[@type="submit"]')
# search_buttton.click()
search_field = driver.find_element(By.XPATH,'//input[@name="q"]')
search_field.send_keys('laptop')
print(search_field.get_attribute('value'))
search_btn = driver.find_element(By.XPATH,'//button[@type="submit"]')
search_btn.click()
sleep(3)

checkbox = driver.find_element(By.XPATH,'//input[@type="checkbox"]/following-sibling::div')
txt = driver.find_element(By.XPATH,'//input[@type="checkbox"]/following-sibling::div/following-sibling::div')
sleep(3)
# search_field.clear()

imgs = driver.find_elements(By.XPATH,'//img[@class="UCc1lI"]')
img = driver.find_element(By.XPATH,'//img[@loading="eager"]')
print(img.get_attribute('src'))


for img in imgs:
    print(img.get_attribute('src'))

checkbox.click()
print(txt.text)
sleep(10)
driver.quit()
