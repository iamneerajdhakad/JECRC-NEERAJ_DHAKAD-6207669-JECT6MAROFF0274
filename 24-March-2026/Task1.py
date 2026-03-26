from time import sleep

## Task 1

### https://codepen.io/gdw96/pen/jOypoYL

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains

opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach',True)

driver = webdriver.Chrome(options=opts)
# 1. navigate to the above url
driver.get('https://codepen.io/gdw96/pen/jOypoYL')
driver.maximize_window()
sleep(1)

wait = WebDriverWait(driver,10)
action = ActionChains(driver)

iframe = wait.until(EC.visibility_of_element_located((By.ID,'result')))
driver.switch_to.frame(iframe)

# 2. enter username and password
username = (wait.until(EC.visibility_of_element_located((By.ID,'username'))))
username.clear()
username.send_keys('student')

email = (wait.until(EC.visibility_of_element_located((By.ID,'email'))))
email.clear()
email.send_keys('student123@gmail.com')

password = (wait.until(EC.visibility_of_element_located((By.ID,'password'))))
password.clear()
password.send_keys('Password123')

# 3. click on hold on the eye to view password
eye_button = wait.until(EC.visibility_of_element_located((By.ID,'showPsswd')))
action.click_and_hold(eye_button).perform()

# 4. click on register
wait.until(EC.visibility_of_element_located((By.XPATH,'//input[@type="submit"]'))).click()

# 5. Use sleep for 5sec then refresh the page
sleep(5)
driver.back()

iframe = wait.until(EC.visibility_of_element_located((By.ID,'result')))
driver.switch_to.frame(iframe)

# 6. Validate the word `Registration` using assert
assert 'Registration' in driver.find_element(By.XPATH,'//div[@class="container"]/h1').text, "failed"

driver.quit()

