from selenium import webdriver
from time import sleep

opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach',True)
opts.add_argument('--headless')
driver = webdriver .Chrome(options=opts)
driver.get('https://vincentgarreau.com/particles.js/')
sleep(4)
print('working fine')