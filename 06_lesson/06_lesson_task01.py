import until
from selenium import webdriver
from selenium.webdriver.common.by import By


browser = webdriver.Chrome()
browser.implicitly_wait(30)
browser.get("http://uitestingplayground.com/ajax")

browser.find_element(By.CSS_SELECTOR, "#ajaxButton").click()

txt = browser.find_element(By.CSS_SELECTOR, '[class="bg-success"]')
print(txt.text)

browser.quit()
