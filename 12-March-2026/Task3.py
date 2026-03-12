# scrip using a loop to print title, name, and current url for all the three browsers

from selenium import webdriver
from time import sleep

browsers = [webdriver.Chrome,webdriver.Edge,webdriver.Firefox]

for browser in browsers:
    driver = browser()
    driver.get('https://vincentgarreau.com/particles.js/')
    print(f'Title for the website is : {driver.title}')
    print(f'Name for the website is : {driver.name}')
    print(f'URL for the website is : {driver.current_url}')
    sleep(2)
    driver.quit()