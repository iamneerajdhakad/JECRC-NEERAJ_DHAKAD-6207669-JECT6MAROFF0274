from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach',True)

driver = webdriver.Chrome(options=opts)
driver.get(r'C:\Python\Testing\Selenium_Framework\20-March-2026\playlist.html')
driver.maximize_window()

select_songs = driver.find_element(By.ID,'songs')
select = Select(select_songs)

if select.is_multiple:
    select.select_by_index(2)
    select.select_by_index(3)
    select.select_by_visible_text('Chlorine')

print(f'List of all the options in select options: {[song.text for song in select.options]}')

print([i.text for i in select.all_selected_options])

driver.find_element(By.XPATH,'//button').click()
