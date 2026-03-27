from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach',True)
opts.add_argument('--headless')
driver = webdriver.Chrome(options=opts)
driver.get('https://vincentgarreau.com/particles.js/')
driver.maximize_window()

sleep(1)

#using ID
icon1 = driver.find_element(By.ID,'icon-codepen-button')
icon2 = driver.find_element(By.ID,'icon-download')
icon3 = driver.find_element(By.ID,'icon-github')
ptcl = driver.find_element(By.ID,'particles-js')
ptcl1 = driver.find_element(By.ID,'js-select-preset')

#using class
label = driver.find_elements(By.CLASS_NAME,'label')
path1 = driver.find_elements(By.CLASS_NAME,'path1')
path2 = driver.find_elements(By.CLASS_NAME,'path2')
path3 = driver.find_elements(By.CLASS_NAME,'path3')
path4 = driver.find_elements(By.CLASS_NAME,'path4')
#using name

des = driver.find_element(By.NAME,'description')
aut = driver.find_element(By.NAME,'author')
view = driver.find_element(By.NAME,'viewport')
data = driver.find_element(By.NAME,'data')
tc = driver.find_element(By.NAME,'twitter:card')

#using tagname
lnk= driver.find_elements(By.TAG_NAME,'link')
meta= driver.find_elements(By.TAG_NAME,'meta')
title= driver.find_elements(By.TAG_NAME,'title')
div= driver.find_elements(By.TAG_NAME,'div')
a= driver.find_elements(By.TAG_NAME,'a')

