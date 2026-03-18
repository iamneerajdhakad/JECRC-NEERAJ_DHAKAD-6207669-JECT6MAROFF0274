## Task 2

### Registration Form

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach',True)

driver = webdriver.Chrome(options=opts)
# 1. Go to: https://demoqa.com/automation-practice-form
driver.get('https://demoqa.com/automation-practice-form')
driver.maximize_window()
sleep(2)

# 2. Handle every element in that form except the calendar
# `Note: Give fake names and emails`

first_name = driver.find_element(By.ID,'firstName')
first_name.send_keys('Hello')
sleep(2)

last_name = driver.find_element(By.ID,'lastName')
last_name.send_keys('World')
sleep(2)

email = driver.find_element(By.ID,'userEmail')
email.send_keys('HelloWorld@gmail.com')
sleep(2)

male_radio_button = driver.find_element(By.XPATH,'//input[@type="radio"]')
male_radio_button.click()
sleep(2)

phone_number = driver.find_element(By.ID,'userNumber')
phone_number.send_keys('1234567890')
sleep(2)

subjects = driver.find_element(By.ID,'subjectsInput')
# subjects.send_keys('Physics') # It was creating problem with this so i commented it out
# subjects.click()
sleep(2)

checkboxes = driver.find_elements(By.XPATH,'//input[@type="checkbox"]')

sleep(1)
for i in range(0,len(checkboxes)):
    if i==1:
        continue
    checkboxes[i].click()
    sleep(1)

upload_picture = driver.find_element(By.ID,'uploadPicture')
upload_picture.send_keys(r'C:\Movies\na\54669.jpg')
sleep(2)

text_area = driver.find_element(By.ID,'currentAddress')
text_area.send_keys('QWERTYUIOPASDFGHJKLZXCVBNMMBVCXZLKJHGFDSAPOIUYTREWQ1234567890')

state_drop_down = driver.find_element(By.ID,'react-select-3-input')
state_drop_down.send_keys('Rajasthan',Keys.ENTER)

city_drop_down = driver.find_element(By.ID,'react-select-4-input')
city_drop_down.send_keys('Jaipur',Keys.ENTER)

# 3. Click on submit button

submit_button = driver.find_element(By.ID,'submit')
submit_button.click()

sleep(5)
driver.quit()