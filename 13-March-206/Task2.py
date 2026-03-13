# TASK-2

from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach',True)
opts.add_argument('--headless')
driver = webdriver.Chrome(options=opts)
# 1.Go to https://the-internet.herokuapp.com/login.
driver.get('https://the-internet.herokuapp.com/login')
print("Sub-Task 1 Successfully Executed!!")

sleep(5)

# 2.Locate the username field using XPath with Tag and name attribute.
username = driver.find_element(By.XPATH,'//input[@name="username"]')
print("Sub-Task 2 Successfully Executed!!")
# 3.Locate the password field using XPath with Tag and id attribute.
password = driver.find_element(By.XPATH,'//input[@id="password"]')
print("Sub-Task 3 Successfully Executed!!")
# 4.Locate the "Login" button using XPath with Tag and type attribute.
button = driver.find_element(By.XPATH,'//button[@type="submit"]')
print("Sub-Task 4 Successfully Executed!!")
# 5.Locate the "Elemental Selenium" link using its exact text with text().
text_field = driver.find_element(By.XPATH,'//a[text()="Elemental Selenium"]')
print("Sub-Task 5 Successfully Executed!!")
# 6.Locate the main heading "Login Page" using contains() with text.
text_field_2 = driver.find_element(By.XPATH,'//h2[text()="Login Page"]')
print("Sub-Task 6 Successfully Executed!!")

# Terminate the session
driver.quit()
