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
sleep(7)

Login_btn = driver.find_element(By.XPATH, "//button[@type='submit']")
Login_btn.click()

sleep(5)
Not_btn = driver.find_element(By.XPATH, "//button[@type='button']")
Not_btn.click()
sleep(5)
Not_btnI = driver.find_element(By.XPATH, "//button[contains(text(), 'Not Now')]")
Not_btnI.click()
sleep(3)
# profile = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/section/nav/div[2]/div/div/div[3]/div/div[6]/div[1]/span/img")
# profile.click()
messages = driver.find_element(By.XPATH, "//a[@aria-label='Direct messaging - 0 new notifications link']")
# messages = driver.find_element(By.XPATH, "//a[@aria-label='Direct messaging - 1 new notifications link']")

messages.click()
sleep(5)
# inbox_text = driver.find_element(By.XPATH, "//span[contains(text(), 'Sent you a message')]")
# inbox_text.click()
# msg_inbox = driver.find_element(By.XPATH, "//svg[@aria-label='Messenger']")
# msg_inbox.click()

# text_inbox = driver.find_element(By.XPATH, "//*[@id='mount_0_0_Kf']/div/div/div/div[1]/div/div/div/div[1]/div[1]/div/section/div/div[2]/div/div/div[1]/div[2]/div/div/div/div/div[2]/a/div")
text_inbox = driver.find_element(By.XPATH, "//div[contains(text(), 'Vishal Singh')]")
text_inbox.click()
sleep(3)
msg_inbox_send = driver.find_element(By.XPATH, "//textarea[@placeholder='Message...']")
msg_inbox_send.send_keys("It's an automated msg to not use this inbox as a meme collection")
sleep(2)
msg_send_btn = driver.find_element(By.XPATH, "//button[contains(text(), 'Send')]")
msg_send_btn.click()

# message_now = driver.find_element(By.XPATH, "//[aria-labelledby='f221cc7407b9a4c f23f45a8d81c0a8 f1a28edb38c8a84 f1809e6c3aa9a28']")
