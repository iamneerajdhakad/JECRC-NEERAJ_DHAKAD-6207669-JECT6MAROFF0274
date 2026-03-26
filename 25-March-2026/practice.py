'''
# Complete Flow On Amazon
# Steps:
# Open website
# Verify homepage title & URL
# Search for product → "Headphones"
# Apply filters (Brand,price(upto 500 or above 1000 anything))
'''

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach',True)

driver = webdriver.Chrome(options=opts)
driver.get('https://www.amazon.in/')
driver.maximize_window()

assert 'amazon' in driver.current_url, "mis-match URL"

wait = WebDriverWait(driver,10)

wait.until(EC.visibility_of_element_located((By.ID,'twotabsearchtextbox'))).send_keys('Headphones',Keys.ENTER)
wait.until(EC.visibility_of_element_located((By.XPATH,'//div[@id="brandsRefinements"]/descendant::span[text()="JBL"]'))).click()
min_max_prices = wait.until(EC.visibility_of_element_located((By.ID,'p_36/range-slider_slider-item_lower-bound-slider')))
driver.execute_script('arguments[0].min="1000";',min_max_prices)

# Open a product → switch to new tab

product_name=wait.until(EC.presence_of_element_located((By.XPATH,'//div[@role="listitem"]/descendant::h2/span'))).text
product_price=wait.until(EC.presence_of_element_located((By.XPATH,'//span[@class="a-price"]/span[@class="a-offscreen"]'))).text

wait.until(EC.visibility_of_element_located((By.XPATH,'//div[@data-cy="title-recipe"]/a'))).click()

all_window = driver.window_handles
driver.switch_to.window(all_window[-1])

# Verify product details (title, price) using assert
assert product_name in driver.find_element(By.XPATH,'//span[@id="productTitle"]').text,'Product not found'
assert product_price in driver.find_element(By.XPATH,"//div[@id='apex_desktop']/descendant::span[@class='a-price-whole']").text, 'Product not found'

# Add to cart

wait.until(EC.visibility_of_element_located((By.ID,'add-to-cart-button'))).click()
wait.until(EC.visibility_of_element_located((By.ID,'nav-cart-count-container'))).click()

# Go to cart verify item (using assert with the name used eailer)
msg = driver.find_element(By.XPATH,'//span[@class="a-truncate sc-grid-item-product-title a-size-base-plus"]/descendant::span[@class="a-truncate-full a-offscreen"]')

assert product_price in wait.until(EC.visibility_of_element_located((By.XPATH,'//span[@class="a-size-medium a-color-base sc-price sc-white-space-nowrap"]'))).text,"Mis-match"
assert product_name in msg.get_attribute("textContent"),"Mis-match"

driver.quit()