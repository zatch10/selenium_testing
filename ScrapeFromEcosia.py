from selenium import webdriver 
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
import csv

timeout = 10
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.ecosia.org/?c=en")
driver.find_element_by_css_selector('.input').send_keys("bangalore yoga gmail.com")
WebDriverWait(driver, timeout).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.button-search-icon')))
driver.find_element_by_css_selector('.button-search-icon').click()
pages = driver.find_elements_by_css_selector('.pagination-button')
i = 1
links = []
while i < 7:
    try:
        pages[i].click()
    except:
        results = driver.find_elements_by_css_selector('.result-url.js-result-url')
        for j in range(len(results)):
            links.append(results[j].text)
        i += 1
driver.quit()
undesired = "https://mail.google.com"
while undesired in links:
    links.remove(undesired)
with open('links_scraped.csv', mode='w') as csv_file:
    for entries in links:
        csv_file.write(entries)
        csv_file.write('\n')