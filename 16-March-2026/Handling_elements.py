from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach',True)

driver = webdriver.Chrome(options=opts)

driver.get('https://testautomationpractice.blogspot.com/')
driver.maximize_window()
sleep(3)
#
# name = driver.find_element(By.ID,'name')
# name.clear()
# name.send_keys('Neeraj')
# # name.clear() clear the input field if it contains
# sleep(1)
# email = driver.find_element(By.XPATH,'//input[@placeholder="Enter EMail"]')
# email.send_keys('temp123@gmail.com')
# sleep(1)
#
# # print(name.get_attribute('name'))
#
# male = driver.find_element(By.ID,'male')
# male.click()

# monday = driver.find_element(By.XPATH,'//label[text()="Monday"]/preceding-sibling::input').click()

genders = driver.find_elements(By.XPATH,'//input[@name="gender"]')

for gender in genders:
    gender.click()
    sleep(2)

check_boxs = driver.find_elements(By.XPATH,'//input[@type="checkbox"]')
check_boxs = check_boxs[:7]
days = driver.find_elements(By.XPATH,'//label[@class="form-check-label"]')
i=2

for check_box in check_boxs:
    check_box.click()
    print(days[i].text)
    i+=1
    sleep(1)
    if(i==9):
        break

check_boxs = check_boxs[::-1]
for check_box in check_boxs:
    check_box.click()
    sleep(1)

sleep(10)
driver.quit()
