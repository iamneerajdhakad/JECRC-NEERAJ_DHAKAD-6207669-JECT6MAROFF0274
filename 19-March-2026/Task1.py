
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach',True)

driver = webdriver.Chrome(options=opts)

driver.get('https://abc.com')
driver.maximize_window()

wait = WebDriverWait(driver,10)

banners = wait.until(EC.presence_of_all_elements_located((By.XPATH,'//div[@id="hero-items"]/descendant::img[@data-mptype="image"]')))

for banner in banners:
    print(banner.get_attribute('src'))