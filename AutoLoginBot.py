from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

def startBot(username, password, url):
    service = Service("C:/Users/HP/Downloads/chromedriver_win32/chromedriver.exe")
    driver = webdriver.Chrome(service=service)

    try:
        driver.get(url)
        driver.find_element(By.NAME, "username").send_keys(username)
        driver.find_element(By.NAME, "password").send_keys(password)
    
    finally:
        driver.quit()

username = "your_username"
password = "your_password"
url = "https://your-login-page.com"
startBot(username, password, url)
