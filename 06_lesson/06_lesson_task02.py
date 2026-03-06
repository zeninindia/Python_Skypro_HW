import until
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



browser = webdriver.Chrome()

browser.get(" http://uitestingplayground.com/textinput")

input_field = browser.find_element(By.CSS_SELECTOR, '[class="form-control"]')

input_field.send_keys("SkyPro")
browser.implicitly_wait(50)
browser.find_element(By.CSS_SELECTOR, "#updatingButton").click()

txt = browser.find_element(By.CSS_SELECTOR, '#updatingButton')

print(txt.text)

browser.quit()
