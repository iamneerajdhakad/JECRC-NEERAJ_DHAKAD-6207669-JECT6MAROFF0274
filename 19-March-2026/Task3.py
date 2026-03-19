# navigate to amzon
# search a product through send_keys But dont click on search or keys.enter
# wait for the suggestion to apperar
#click on 4th suggestion
#click on sort by and click on newest
# click on free shipping check box
# wait for first product  and return me the name = price (without using inner text)

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach',True)

driver = webdriver.Chrome(options=opts)

driver.get('https://www.amazon.in/')
driver.maximize_window()

wait = WebDriverWait(driver,15)

search_button = wait.until(EC.visibility_of_element_located((By.ID,'twotabsearchtextbox')))
search_button.send_keys('laptop')

suggestion = wait.until(EC.visibility_of_element_located((By.ID,'sac-suggestion-row-4')))
suggestion.click()

sort_button = wait.until(EC.visibility_of_element_located((By.XPATH,'(//span[@class="a-button-inner"])[2]')))
sort_button.click()
newest_button = wait.until(EC.visibility_of_element_located((By.ID,'s-result-sort-select_4')))
newest_button.click()

free_shipping_checkbox = wait.until(EC.visibility_of_element_located((By.XPATH,'//label/input[@type="checkbox"]/following-sibling::i')))
free_shipping_checkbox.click()

product_name = wait.until(EC.visibility_of_element_located((By.XPATH,'//div[@data-cy="title-recipe"]/descendant::h2/span')))
print(f'Name of the first product is: {product_name.text}')
product_price = wait.until(EC.visibility_of_element_located((By.XPATH,'//span[@id="price-link"]/following-sibling::a/span')))
print(f'Price of the Product is: {product_price.text}')



