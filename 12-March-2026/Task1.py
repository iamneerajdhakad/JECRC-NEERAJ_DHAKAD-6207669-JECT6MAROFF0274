#script  perform all the function in chrome
from attr.converters import optional

from selenium import webdriver
from time import sleep

opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach',True)
driver = webdriver.Chrome(options=opts)
driver.get('https://vincentgarreau.com/particles.js/')
driver.maximize_window()
driver.back()
sleep(2)
driver.forward()
sleep(2)
driver.refresh()
sleep(2)
driver.minimize_window()

driver.quit()

