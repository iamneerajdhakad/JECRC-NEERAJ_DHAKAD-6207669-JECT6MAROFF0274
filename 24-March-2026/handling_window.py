from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach',True)
driver = webdriver.Chrome(options=opts)
driver.get('https://the-internet.herokuapp.com/windows')
driver.maximize_window()
sleep(2)

driver.find_element(By.XPATH,'//a[text()="Click Here"]').click()
sleep(2)
cur_window = driver.current_window_handle
all_windows = driver.window_handles
print(all_windows)

driver.switch_to.window(all_windows[-1])
assert 'New' in driver.find_element(By.TAG_NAME,'div').text, "Failed"
driver.close()

driver.switch_to.window(cur_window)
driver.find_element(By.XPATH,'//a[text()="Click Here"]').click()

driver.switch_to.new_window('window')
sleep(5)
driver.get('https://abc.com')

driver.switch_to.new_window('tab')
sleep(5)
driver.get('https://google.com')
