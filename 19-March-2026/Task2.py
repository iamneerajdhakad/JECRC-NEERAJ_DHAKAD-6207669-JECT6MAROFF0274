
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach',True)

driver = webdriver.Chrome(options=opts)

driver.get('https://qavbox.github.io/demo/signup/')
driver.maximize_window()

wait = WebDriverWait(driver,10)

first_name = wait.until(EC.visibility_of_element_located((By.ID,'username')))
first_name.send_keys('Hello')

email = wait.until(EC.visibility_of_element_located((By.ID,'email')))
email.send_keys('HelloWorld@gmail.com')

phone_no = wait.until(EC.visibility_of_element_located((By.ID,'tel')))
phone_no.send_keys('1234567890')

upload_button = wait.until(EC.visibility_of_element_located((By.XPATH,'//input[@type="file"]')))
upload_button.send_keys(r'C:\Movies\na\54669.jpg')

gender_drop_down = wait.until(EC.visibility_of_element_located((By.XPATH,'//select[@name="sgender"]')))
select_gender = Select(gender_drop_down)
select_gender.select_by_value('male')

radio_button = wait.until(EC.visibility_of_element_located((By.XPATH,'//input[@value="five"]')))
radio_button.click()

checkboxes = wait.until(EC.visibility_of_all_elements_located((By.XPATH,'//input[@type="checkbox"]')))

for checkbox in checkboxes:
    if 'Testing' in checkbox.text:
        checkbox.click()

select_Tool = wait.until(EC.visibility_of_element_located((By.XPATH,'//select[@id="tools"]')))
Tool = Select(select_Tool)
Tool.select_by_value('selenium')

submit_button = wait.until(EC.element_to_be_clickable((By.ID,'submit')))
submit_button.click()
