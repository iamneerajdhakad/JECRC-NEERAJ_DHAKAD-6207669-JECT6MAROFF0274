from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach',True)

driver = webdriver.Chrome(options=opts)
driver.get('https://demoqa.com/droppable')

driver.maximize_window()
sleep(3)
wait = WebDriverWait(driver,10)

drag_me = wait.until(EC.visibility_of_element_located((By.ID,'draggable')))
dropped = wait.until(EC.visibility_of_element_located((By.ID,'droppable')))

action = ActionChains(driver)
action.drag_and_drop(drag_me,dropped).perform()


# assert 'Dropped!' == driver.find_element(By.ID,'droppable').text, 'Action Failed'
