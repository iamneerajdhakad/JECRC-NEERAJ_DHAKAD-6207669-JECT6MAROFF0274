#To open Edge browser

from  selenium import webdriver
from time import sleep

# driver = webdriver.Edge()
# sleep(5)
#
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



opts = webdriver.EdgeOptions()
opts.add_experimental_option('detach',True)
driver = webdriver.Edge(options=opts)
driver.get('https://vincentgarreau.com/particles.js/')
driver.maximize_window()


driver.quit()

