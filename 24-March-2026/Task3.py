
## Task 3

### Windows
#
# 1. navigate to the url: `https://demoqa.com/browser-windows`
# 2. work on all the 3 windows one after the other
# 3. validate the text result appearing, you should use assert with it the result shown

from selenium import webdriver
from selenium.webdriver.common.by import By

opts = webdriver.ChromeOptions()
# opts.add_experimental_option('detach',True)

driver = webdriver.Chrome()
driver.get('https://demoqa.com/browser-windows')
driver.maximize_window()


home_window = driver.current_window_handle

driver.find_element(By.ID,'tabButton').click()
all_window = driver.window_handles
driver.switch_to.window(all_window[1])
window_1 = driver.find_element(By.TAG_NAME,'h1')
assert 'sample page' in window_1.text, "Window_1 not selected"

driver.switch_to.window(home_window)

driver.find_element(By.ID,'windowButton').click()
all_window = driver.window_handles
driver.switch_to.window(all_window[2])
window_2 = driver.find_element(By.TAG_NAME,'h1')
assert 'sample page' in window_2.text, "Window_1 not selected"

driver.switch_to.window(home_window)

driver.find_element(By.ID,'messageWindowButton').click()
# all_window = driver.window_handles
# driver.switch_to.window(all_window[-1])
# window_3 = driver.find_element(By.XPATH,'//body')
# print(window_3.get_attribute("textContent"))
# assert 'Knowledge' in window_3.get_attribute("innerText"), "Window_1 not selected"

driver.switch_to.window(home_window)
driver.quit()