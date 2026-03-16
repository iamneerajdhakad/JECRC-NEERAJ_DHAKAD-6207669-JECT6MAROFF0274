from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach',True)
opts.add_argument('--headless')
driver = webdriver.Chrome(options=opts)
# 1. Navigate to https://www.amazon.in/
driver.get('https://www.amazon.in/')
print("Sub-Task 1 Successfully Executed!!")
driver.maximize_window()
sleep(5)

## finding ancestor
driver.find_element(By.XPATH,'//span[text()="All"]/ancestor::div[@id="nav-main"]')
print("ANCESTOR FOUND")

#finding decendent
driver.find_element(By.XPATH,'//div[@id="nav-xshop"]/descendant::a[text()="Bestsellers"]')
driver.find_element(By.XPATH,'//div[@class="nav-div"]/descendant::a[text()="Fresh"]')
print("DECENDANT FOUND")

#finding siblings (preceding / following)
driver.find_element(By.XPATH,'//a[text()="Fresh"]/ancestor::li/following-sibling::li[1]')


driver.quit()