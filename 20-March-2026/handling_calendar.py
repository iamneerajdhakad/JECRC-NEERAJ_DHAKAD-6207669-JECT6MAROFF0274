
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach',True)

driver = webdriver.Chrome(options=opts)


driver.get('https://testautomationpractice.blogspot.com/')
driver.maximize_window()

driver.find_element(By.ID,'datepicker').send_keys('01/01/2001',Keys.ENTER)

driver.find_element(By.ID,'txtDate').click()

select_year = Select(driver.find_element(By.XPATH,'//select[@class="ui-datepicker-year"]'))
print(f"Year names: {[i.text for i in select_year.options]}")
year = input("Enter Year")
select_year.select_by_visible_text(year)

select_month = Select(driver.find_element(By.XPATH,'//select[@class="ui-datepicker-month"]'))
print(f"Month names: {[i.text for i in select_month.options]}")
month = input("Enter a month")
select_month.select_by_visible_text(month)

select_date = driver.find_elements(By.XPATH,'//table[@class="ui-datepicker-calendar"]/tbody/descendant::a')
print(f"Valid dates: {[i.text for i  in select_date]}")
date = int(input("Enter date"))

driver.find_element(By.XPATH,f'//a[text()={date}]').click()



