from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


browser = webdriver.Chrome()
browser.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")

element = WebDriverWait(browser, 40).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "#landscape"))
    )
src = browser.find_element(By.CSS_SELECTOR, '#award')
print(src.get_attribute('src'))

browser.quit()
