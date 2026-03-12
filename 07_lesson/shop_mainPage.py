from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class MainPage():
  def __init__(self, driver):
    self.driver = driver
    self.wait = WebDriverWait(self.driver, 50)

  def choose_items(self, element):
      elements = {
          "Backpack": "add-to-cart-sauce-labs-backpack",
          "T-Shirt": "add-to-cart-sauce-labs-bolt-t-shirt",
          "Onesie": "add-to-cart-sauce-labs-onesie",
      }
      if element in elements:
         self.driver.find_element(
                  By.NAME, elements[element]).click()

  def cart(self):
      self.driver.find_element(
          By.CSS_SELECTOR, '.shopping_cart_link').click()

