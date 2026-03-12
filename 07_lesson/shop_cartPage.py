from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class CartPage:
  def __init__(self, driver):
    self.driver = driver
    self.wait = WebDriverWait(self.driver, 50)
    self.driver.maximize_window()

  def checkout(self):
      self.driver.find_element(
          By.ID, "checkout").click()
