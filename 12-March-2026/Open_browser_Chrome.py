#To open Chrome browser

from  selenium import webdriver
from time import sleep

# driver = webdriver.Chrome()
# driver.get('https://github.com/')
# driver.maximize_window()
# sleep(2)
#
# driver.back()
# sleep(2)
# driver.forward()
# sleep(2)
# driver.refresh()
# sleep(2)
#
# driver.minimize_window()
# sleep(2)
opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach',True)
driver = webdriver.Chrome(options=opts)
driver.get('https://vincentgarreau.com/particles.js/')
driver.maximize_window()
print(f'Title of the website is : {driver.title}')
sleep(5)
driver.quit()