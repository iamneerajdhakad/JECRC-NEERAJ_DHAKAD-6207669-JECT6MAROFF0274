#use all the locators in one script using one website

from selenium import webdriver
from selenium.webdriver.common.by import By

from time import sleep

opts=webdriver.ChromeOptions()
opts.add_experimental_option('detach',True)
# opts.add_argument('--headless')
driver=webdriver.Chrome(options=opts)
driver.get('https://www.cricbuzz.com/')
driver.maximize_window()
sleep(5)

#By using ID
element1=driver.find_element(By.ID,'shosh')
print("element shosh found by ID")
element2=driver.find_element(By.ID,'main-header')
print("main header found by ID")

#By using name
element3=driver.find_element(By.NAME,'viewport')
elements4=driver.find_elements(By.NAME,'robots')
print("viewport element found by name")
print("robots element found by name")
print(elements4)
print(len(elements4))
element5=driver.find_element(By.NAME,'description')
print("description found by name")

#by using class
element6=driver.find_element(By.CLASS_NAME,'min-h-container')
print("Class min-h-container found")
element7=driver.find_element(By.CLASS_NAME,'col-span-9')
print("Class col-span-9 found")
element8=driver.find_elements(By.CLASS_NAME,'col-span-9')
print(f"Class col-span-9 has {len(element8)} elements")

#by using tag name
element9=driver.find_element(By.TAG_NAME,'img')
print("Tag image found")
element10=driver.find_element(By.TAG_NAME,'button')
print("Tag button found")
elements11=driver.find_elements(By.TAG_NAME,'a')
print(f"Found {len(elements11)} elements with anchor tag")

#Using CSS locator
element12=driver.find_element(By.CSS_SELECTOR,'button[class*=bg')
print("CSS element found - button with class containing bg")
element13=driver.find_element(By.CSS_SELECTOR,'a[href*="cricket-schedule"]')
print("CSS element found - link for cricket schedule")

#Using Xpath
element14=driver.find_element(By.XPATH,'//a[@title="India vs New Zealand, Final "]')
print("Element found using Xpath - element with title India vs New Zealand, Final ")
element15=driver.find_elements(By.XPATH,'span[text()="Log In"]')
print("Element found using Xpath - element with Log in in the inline text")

