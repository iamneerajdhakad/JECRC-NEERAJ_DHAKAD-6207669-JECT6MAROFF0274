'''
explicit wat : It is a conditional wait
                It is not a global wait it is bound to a pariticular element
                It throws Time Out exception
'''
from gc import enable

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach',True)

driver = webdriver.Chrome(options=opts)

# driver.get('https://abc.com')
# driver.maximize_window()
#
# wait = WebDriverWait(driver,10)

# loading_circles = wait.until(EC.invisibility_of_element_located((By.ID,'preloader-animated_svg__svg3')))
# title_abc = driver.find_element(By.XPATH,'//span[text()="ABC SHOWS, SPECIALS & MORE"]')
#
# assert 'SPECIALS' in title_abc.text, 'the title does not contains SPECIALS'

# print('working fine')

driver.get('https://demoqa.com/dynamic-properties')
driver.maximize_window()

wait = WebDriverWait(driver,4)

enable_button = driver.find_element(By.ID,'enableAfter')
print(enable_button.is_enabled())
enable_button = wait.until(EC.element_to_be_clickable((By.ID,'enableAfter')))
if enable_button.is_enabled():
    enable_button.click()
    print(enable_button.text)
else:
    print('button not enabled')

visible_element = wait.until(EC.visibility_of_element_located((By.ID,'visibleAfter')))


driver.quit()