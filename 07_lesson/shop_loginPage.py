from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 50)
        self.driver.maximize_window()
        self.driver.get("https://www.saucedemo.com/")

    def log(self, login, password):
        self.driver.find_element(
            By.CSS_SELECTOR, '[name="user-name"]').send_keys(login)
        self.driver.find_element(
            By.CSS_SELECTOR, '[name="password"]').send_keys(password)

    def login(self):
        self.driver.find_element(
            By.CSS_SELECTOR, '[name="login-button"]').click()
