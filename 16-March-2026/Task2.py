# Task 2
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach',True)
driver = webdriver.Chrome(options=opts)

# 1. Open the radio button page.
driver.get('https://demoqa.com/radio-button')
driver.maximize_window()
sleep(3)

# 2. Print the **title** of the page.
print(f'Title of the web page: {driver.title}')
sleep(1)

# 3. Locate the **"Yes" radio button**.
yes_radio_button = driver.find_element(By.ID,'yesRadio')

# 4. Click the radio button using `click()`.
yes_radio_button.click()
sleep(1)

# 5. Capture and print the **result message** using `.text`.
result_message = driver.find_element(By.XPATH,'//p[@class="mt-3"]')
print(result_message.text)
sleep(1)

# 6. Use `get_attribute()` to fetch attributes like:
#    - `class`
#    - `id`

print(f'ID attribute: {yes_radio_button.get_attribute('id')}')
print(f'CLASS attribute: {result_message.get_attribute('class')}')


# 7. Print the **current URL**.
print(f'current URL of the page : {driver.current_url}')

sleep(10)
driver.quit()