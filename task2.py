from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException  
import time

#edit username password here before running the bot
username = ""
password = ""

#initializing wait and driver
driver = webdriver.Firefox()
driver.maximize_window()
wait = WebDriverWait(driver,15)

def check_100(item):
    try:
        driver.find_element_by_css_selector(item)
    except NoSuchElementException:
        return False
    return True

#getting login website
driver.get("https://www.instagram.com/accounts/login/")

#page wait to ensure variable has been loaded
page_wait = wait.until(EC.presence_of_element_located(
    (By.CLASS_NAME, "KPnG0")))

#login
user = driver.find_element_by_name('username')
user.clear()
user.send_keys(username)

pas = driver.find_element_by_name('password')
pas.clear()
pas.send_keys(password)

#page wait to ensure login button is present
page_wait = wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[4]')))
driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[4]/button').click()
time.sleep(3)

#once logged in opening the other page
driver.get("https://www.instagram.com/emmawatson")
page_wait = wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a')))

driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a').click()

#scrolling down the pop to find the 100th user
while True:
    time.sleep(1)
    popup = driver.find_element_by_xpath('/html/body/div[3]/div//a')
    check = check_100("li.wo9IH:nth-child(100)")
    if check == True:
        break
    popup.send_keys(Keys.END)
    time.sleep(1)

#after checking for 100th user, click on the user link
user_100 = driver.find_element_by_xpath("/html/body/div[3]/div/div[2]/ul/div/li[100]/div/div[1]/div[2]/div[1]/a").click()

page_wait = wait.until(EC.element_to_be_clickable((By.XPATH,'/html/body/span/section/main/div/header/section/div[1]/div[1]/span/span[1]/button')))

#click on follow (the xpath is same for any instagram header)
driver.find_element_by_xpath("/html/body/span/section/main/div/header/section/div[1]/div[1]/span/span[1]/button").click()

