from selenium import webdriver
from selenium.webdriver.common import alert
from selenium.webdriver.common.by import By
from time import sleep



browser = webdriver.Firefox()
browser.get("http://the-internet.herokuapp.com/login")

sleep(1)
input_field_name = browser.find_element(By.CSS_SELECTOR, "[name='username']")
input_field_name.clear()
input_field_name.send_keys("tomsmith")
sleep(1)
input_field_password = browser.find_element(By.CSS_SELECTOR, "[name='password']")
input_field_password.clear()
input_field_password.send_keys("SuperSecretPassword!")

sleep(1)
browser.find_element(By.CSS_SELECTOR, "[class='radius']").click()
sleep(1)
message_news = browser.find_element(By.CSS_SELECTOR, "[class='flash success']")

print(message_news.text)

browser.quit()
