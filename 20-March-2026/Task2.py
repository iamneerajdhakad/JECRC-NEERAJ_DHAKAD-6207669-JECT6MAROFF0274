from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach',True)

driver = webdriver.Chrome(options=opts)
driver.get(r'C:\Python\Testing\Selenium_Framework\20-March-2026\playlist.html')
driver.maximize_window()

select_songs = driver.find_element(By.ID,'songs')
avicii = driver.find_elements(By.XPATH,'//select/descendant::optgroup[@label="Avicii"]/option')
select = Select(select_songs)

if select.is_multiple:
    for song in avicii:
        select.select_by_visible_text(song.text)

driver.find_element(By.XPATH,'//button').click()