import  selenium
from selenium import  webdriver
from selenium.webdriver.common.by import  By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from time import sleep

PATH = "C:\Program Files (x86)\chromedriver.exe"
options = Options()

PROXY = "proxy.soax.com:10002"
options = webdriver.ChromeOptions()
options.add_argument('proxy.soax.com'.format(PROXY))
driver = webdriver.Chrome(service=Service(PATH), options=options)

driver.get("https://instagram.com/")
sleep(3)

username = driver.find_element(By.XPATH, "//input[@type='text']")
password = driver.find_element(By.XPATH, "//input[@type='password']")
username.send_keys('___klaus_3.1452')
password.send_keys('Doll@2005')
sleep(3)

Login_btn = driver.find_element(By.XPATH, "//button[@type='submit']")
Login_btn.click()

sleep(5)
Not_btn = driver.find_element(By.XPATH, "//button[@type='button']")
Not_btn.click()
sleep(5)
Not_btnI = driver.find_element(By.XPATH, "//button[contains(text(), 'Not Now')]")
Not_btnI.click()
sleep(3)
profile = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/section/nav/div[2]/div/div/div[3]/div/div[6]/div[1]/span/img")
profile.click()
