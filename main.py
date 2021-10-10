from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException

import time
import random

comments_ = ["Awesome!!", "Cool!", "Wadhiv!","Love it!!"]

EMAIL = "sidkulkarnimj@gmail.com"
PASSWORD = "9881823532"

chrome_driver_path = "F:/chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get("https://www.instagram.com/")
time.sleep(3)





log_in_fb = driver.find_element_by_xpath("//button/span[text()='Log in with Facebook']")
log_in_fb.click()
time.sleep(2)

log_in = driver.find_element_by_xpath('//div/input[@id="email"]')
log_in.click()
log_in.send_keys(EMAIL)
time.sleep(5)

password = driver.find_element_by_xpath('//div/input[@id="pass"]')
password.click()
password.send_keys(PASSWORD)
password.send_keys(Keys.ENTER)
time.sleep(10)

notification_window = driver.find_element_by_xpath('//button[text()="Not Now"]')
notification_window.click()
time.sleep(10)

search1 = driver.find_element_by_xpath('//span[text()="Search"]')
search1.click()
time.sleep(1)

search = driver.find_element_by_xpath('//input[@placeholder="Search"]')
search.click()
time.sleep(3)

search.send_keys("dev__yogesh")

count = 0
while count< 3:
    search.send_keys(Keys.ENTER)
    count += 1
    time.sleep(1)

first_element = driver.find_element_by_xpath('//div[@class="_9AhH0"]')
first_element.click()
time.sleep(2)


def like_comment():

    like = driver.find_element_by_xpath('//button[@class="wpO6b  "]//*[@aria-label="Like"]')
    like.click()
    time.sleep(2)

    comment = driver.find_element_by_xpath('//div[@class="RxpZH"]')
    comment.click()
    time.sleep(2)

    comment2 = driver.find_element_by_class_name("Ypffh")
    comment2.send_keys(random.choice(comments_))

    post = driver.find_element_by_xpath('//button[text()="Post"]')
    post.click()
    time.sleep(2)

    next = driver.find_element_by_xpath('//a[text()="Next"]')
    next.click()
    time.sleep(5)

try:
    like_comment()
    time.sleep(2)
except ElementClickInterceptedException:
    cancel_button = driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[3]/button[2]')
    cancel_button.click()


close_ = driver.find_element_by_xpath('//button[@class="wpO6b  "]//*[@aria-label="Close"]')
close_.click()
