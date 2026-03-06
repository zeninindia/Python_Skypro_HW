from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By


browser = webdriver.Chrome()
browser.get("http://uitestingplayground.com/ajax")

pause = WebDriverWait(browser, 40)

browser.find_element(By.CSS_SELECTOR, "#ajaxButton").click()

pause.until(
    EC.text_to_be_present_in_element( (By.CSS_SELECTOR, '[class="bg-success"]'), "Data loaded with AJAX get request.")
)

txt = browser.find_element(By.CSS_SELECTOR, '[class="bg-success"]')
print(txt.text)

browser.quit()
