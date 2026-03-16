## Task1
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach',True)
driver = webdriver.Chrome(options=opts)
driver.maximize_window()

# 1. Open the OrangeHRM demo website. `https://opensource-demo.orangehrmlive.com/`
driver.get('https://opensource-demo.orangehrmlive.com/')
sleep(3)

# 2. Get and print the title of the page.
print(f'Title of the web page: {driver.title}')
sleep(1)

# 3. Locate the username input field and use clear() if needed.
username = driver.find_element(By.XPATH,'//input[@name="username"]')
username.clear()

# 4. Enter the username using send_keys().
username.send_keys('Admin')
sleep(1)

# 5. Locate the password input field and enter the password using send_keys().
password = driver.find_element(By.XPATH,'//input[@name="password"]')
password.send_keys('admin123')
sleep(1)

# 6. Submit the login form using either: click() on the Login button, or Keys.ENTER
driver.find_element(By.XPATH,'//button[@type="submit"]').click()
sleep(1)

# 7. After login, print the current URL.
url = driver.current_url
print(f'current URL of the page : {url}')

# 8. Check if dashboard is present in that url using `in`
print('dashboard' in url)

# 9. Print 'successful login'
print('successful login')
sleep(10)
driver.quit()