## Task 1
from time import sleep

### Booking a Flight Ticket

# 1. Open website (MakeMyTrip)
# 2. Verify the current url
# 3. Select trip type → One Way if not selected
# 4. Enter:
# From city,
# To city,
# Departure date (calendar handling, if next arrow is showing stale element use action chains by moving to arrow then action.click(ele).perform)
# 5. Click Search Flights
# 6. Wait for results page (handle the loading)
# 7. Fetch me the first flight

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach',True)

driver = webdriver.Chrome(options=opts)
driver.get('https://www.cleartrip.com/')
driver.maximize_window()

assert 'trip' in driver.current_url,"URL mis-match"

wait = WebDriverWait(driver,20)

wait.until(EC.visibility_of_element_located((By.XPATH,'//div[@class="pb-1 px-1 flex flex-middle nmx-1"]'))).click()

from_city = wait.until(EC.visibility_of_element_located((By.XPATH,'//input[@placeholder="Where from?"]')))
from_city.click()
from_city.send_keys('Jaipur')
wait.until(EC.element_to_be_clickable((By.XPATH,'//ul[@class="airportList"]/descendant::p[contains(text(),"Jaipur")]'))).click()

to_city = wait.until(EC.visibility_of_element_located((By.XPATH,'//input[@placeholder="Where to?"]')))
to_city.click()
to_city.send_keys('Pune')
wait.until(EC.element_to_be_clickable((By.XPATH,'//ul[@class="airportList"]/descendant::p[contains(text(),"Pune")]'))).click()

calendar = wait.until(EC.visibility_of_element_located((By.XPATH,'//div[@data-testid="dateSelectOnward"]')))
calendar.click()

action = ActionChains(driver)

while True:

    months = wait.until(EC.visibility_of_all_elements_located((By.XPATH,'//div[@class="DayPicker-Caption"]/div')))

    if 'July 2026' in months[0].text or 'July 2026' in months[1].text:
        wait.until(EC.visibility_of_element_located((By.XPATH,'//div[@class="DayPicker-Day"]/descendant::div[text()="1"]'))).click()
        break

    else:
        arrow = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,'div[class="flex-1 ta-right"] svg')))
        action.move_to_element(arrow).click().perform()

wait.until(EC.visibility_of_element_located((By.XPATH,'//button[@class="sc-dhKdcB jkDAfz flex-1"]'))).click()

first_flight = wait.until(EC.visibility_of_element_located((By.XPATH,'//div[@class="sc-aXZVg bCDQyH pt-1 flex flex-between pl-6"]/descendant::p'))).text
print(f'The first flight is: {first_flight}')