from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

URL = "https://tinder.com/app/recs"
EMAIL = os.environ.get("EMAIL")
PASSWORD = os.environ.get("PASSWORD")

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(chrome_options)
driver.get(url=URL)

time.sleep(4)
login_button = driver.find_element(By.XPATH,
                                   value='//*[@id="q1413426407"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]')
login_button.click()

time.sleep(2)
login_options = driver.find_element(By.XPATH,
                                    value='//*[@id="q-314954669"]/div/div/div/div[1]/div/div/div[2]/div[2]/span/button')
login_options.click()

time.sleep(2)
using_FB = driver.find_element(By.XPATH,
                               value='//*[@id="q-314954669"]/div/div[1]/div/div[1]/div/div/div[2]/div[2]/span/div[2]/button')
using_FB.click()

time.sleep(2)
base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)

time.sleep(4)
email_input = driver.find_element(By.XPATH, value='//*[@id="email"]')
email_input.send_keys(EMAIL)
pass_input = driver.find_element(By.XPATH, value='//*[@id="pass"]')
pass_input.send_keys(PASSWORD)

time.sleep(2)
FB_login = driver.find_element(By.XPATH, value='//*[@id="loginbutton"]')
FB_login.click()

driver.switch_to.window(base_window)

time.sleep(4)
accept_button = driver.find_element(By.XPATH, value='//*[@id="q-314954669"]/div/div[2]/div/div/div[1]/div[1]/button')
accept_button.click()

time.sleep(6)
allow_button = driver.find_element(By.XPATH,
                                   value='//*[@id="q-314954669"]/div/div/div/div/div[3]/button[1]/div[2]/div[2]/div')
allow_button.click()

time.sleep(2)
cancel_notification = driver.find_element(By.XPATH,
                                          value='//*[@id="q-314954669"]/div/div/div/div/div[3]/button[2]/div[2]/div[2]/div')
cancel_notification.click()

for n in range(100):

    try:
        time.sleep(10)
        like_button = driver.find_element(By.XPATH,
                                          value='//*[@id="q1413426407"]/div/div[1]/div/div/main/div/div/div[1]/div/div[3]/div/div[4]')
        like_button.click()

    except ElementClickInterceptedException:
        try:
            match_popup = driver.find_element(By.CSS_SELECTOR, value=".itsAMatch a")
            match_popup.click()
        except NoSuchElementException:
            time.sleep(2)
driver.quit()