## Task 1
### Link Text & Partial Link Text

from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach',True)

driver = webdriver.Chrome(options=opts)

# 1. Go to https://the-internet.herokuapp.com/
driver.get('https://the-internet.herokuapp.com/')
driver.maximize_window()
sleep(2)

# 2. Find the "Checkboxes" link using LINK_TEXT
Checkboxes = driver.find_element(By.LINK_TEXT,'Checkboxes')

# 3. Find the "Drag and Drop" link using PARTIAL_LINK_TEXT
Drag_and_Drop = driver.find_element(By.PARTIAL_LINK_TEXT,'Drag')

# 4. Find how many <li> (list item) elements are on the page using find_elements and TAG_NAME. Print the count.
Total_list_items = driver.find_elements(By.TAG_NAME,'li')
print(f'The Total li elements are: {len(Total_list_items)}')

# 5. Navigate to https://the-internet.herokuapp.com/tables
tables = driver.find_element(By.PARTIAL_LINK_TEXT,'Tables')
tables.click()

# 6. Write an XPath to find the "Web Site" (td) for the person with email "jdoe@hotmail.com" in table 1 (Hint: Use text() and ancestor/following sibling or preceding-sibling).
web_site = driver.find_element(By.XPATH,'//td[text()="jdoe@hotmail.com"]/following-sibling::td[2]')

# 7. Write an XPath to find the Delete link (a) for the person with Last Name "Bach" in table 1.
Delete_link = driver.find_element(By.XPATH,'//td[text()="Bach"]/following-sibling::td[5]/a[2]')

# 8. Write an XPath to find the second table `(<table>)` on the page using indexing.
table = driver.find_element(By.XPATH,'//table[2]')

# 9. Write an XPath to find the cell containing "$100.00" in table 2. Find its parent <tr> element.
parent_tr_element = driver.find_element(By.XPATH,'//table/following-sibling::table/descendant::tbody/descendant::tr[3]/td[4]')

driver.quit()