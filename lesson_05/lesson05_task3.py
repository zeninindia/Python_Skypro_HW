from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep



browser = webdriver.Firefox()
browser.get("http://the-internet.herokuapp.com/inputs")

sleep(2)
input_field = browser.find_element(By.CSS_SELECTOR, "[type='number']")
input_field.clear()
input_field.send_keys("12345")
sleep(2)
input_field.clear()
input_field.send_keys("54321")
sleep(2)
browser.quit()
