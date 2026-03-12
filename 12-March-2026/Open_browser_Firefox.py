#To open Firefox browser

from  selenium import webdriver
from time import sleep

# driver = webdriver.Firefox()
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

opts = webdriver.FirefoxOptions()
opts.add_argument('detach')
driver = webdriver.Firefox(options=opts)
driver.get('https://vincentgarreau.com/particles.js/')
driver.maximize_window()

driver.quit()