# create a list and close a url using all browsers

from selenium import webdriver
from time import sleep

browsers = [webdriver.Chrome,webdriver.Edge,webdriver.Firefox]

for browser in browsers:
    driver = browser()
    driver.get('https://vincentgarreau.com/particles.js/')
    sleep(2)
    driver.quit()