from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


browser = webdriver.Chrome()
browser.get("http://uitestingplayground.com/classattr")

sleep(2)
browser.find_element(By.CSS_SELECTOR, ".btn-primary").click()
sleep(2)

browser.quit()
