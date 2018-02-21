#step1 - login through facebook
#step2 - sign in tinder
#step3 - swipe through profiles




import time
import pyautogui
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#clicks chromes allow location pop up
def clickLocationAllow():
    pyautogui.keyDown('Tab')
    pyautogui.keyUp('Tab')
    time.sleep(1)
    pyautogui.keyDown('Enter')
    pyautogui.keyUp('Enter')

browser = webdriver.Chrome('C:\chromedriver')

#step1

browser.get('https://facebook.com')
user_name = browser.find_element_by_id('email')
user_name.send_keys("facebook email")

password= browser.find_element_by_id('pass')
password.send_keys("facebook password")

login_button = browser.find_element_by_id("loginbutton")
login_button.click()

browser.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 't')

#step2

browser.get('https://tinder.com/app/login')
time.sleep(10)

browser.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[2]/div[1]/div/div[3]/button[1]/span').click()
time.sleep(10)
next1 = browser.find_element_by_xpath('//*[@id="content"]/div/span/div/div[2]/div/div[1]/div[1]/div/button')
next1.click()
time.sleep(3)
next2 = browser.find_element_by_xpath('//*[@id="content"]/div/span/div/div[2]/div/div/main/div/button')
next2.click()
next3 = browser.find_element_by_xpath('//*[@id="content"]/div/span/div/div[2]/div/div/div[1]/div/div/div[4]/button[1]')
next3.click()
time.sleep(3)
next4 = browser.find_element_by_xpath('//*[@id="content"]/div/span/div/div[2]/div/div/div[1]/div/div/div[4]/button[1]')
next4.click()
clickTab()
time.sleep(3)

#step3




time.sleep(10)
browser.quit()
