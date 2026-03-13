#TASK-3
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

# 2. Locate the main search bar using its ID with a CSS Selector.
search_bar = driver.find_element(By.CSS_SELECTOR,'#twotabsearchtextbox')
print("Sub-Task 2 Successfully Executed!!")

# 3. Locate the Amazon logo (usually an <a> tag with an ID like nav-logo sprites) using a CSS Selector.
driver.find_element(By.CSS_SELECTOR,'a[id="nav-logo-sprites"]')
print("Sub-Task 3 Successfully Executed!!")

# 4. Locate the "Cart" link/icon (often has an ID like nav-cart) using a CSS Selector.
driver.find_element(By.CSS_SELECTOR,'a[id="nav-cart"]')
print("Sub-Task 4 Successfully Executed!!")

# 5. Locate the "Sign in" link in the navigation bar (It might be inside a div with an ID like nav-tools. Use descendant way (space)).
driver.find_element(By.CSS_SELECTOR,'#nav-tools')
print("Sub-Task 5 Successfully Executed!!")

# 6. Locate all the main category links in the navigation bar under "All"(e.g."Best Sellers", "Mobiles", "Today's Deals").
categories = driver.find_elements(By.CSS_SELECTOR,'li[class="nav-li"]')
print("Sub-Task 6 Successfully Executed!!")
# Inspect their common parent and use descendant way and to find all the <a> tags within it.Use find_elements and print the count.
print(f'Total Categories: {len(categories)}')

driver.quit()
