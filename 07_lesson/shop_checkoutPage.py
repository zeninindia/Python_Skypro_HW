import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver
        self.driver.implicitly_wait(5)
        # self.wait = WebDriverWait(self.driver, 50)


    def name_fields(self, f_name, l_name, zipp):
        self.driver.find_element(
            By.ID, "first-name").send_keys(f_name)
        self.driver.find_element(
            By.ID, "last-name").send_keys(l_name)
        self.driver.find_element(
            By.ID, "postal-code").send_keys(zipp)


    def cont(self):
        self.driver.find_element(
            By.CSS_SELECTOR, '[name="continue"]').click()

