from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class CalculatorPage:
    def __init__(self, driver):
        self.driver = driver

        self.driver.maximize_window()

    def open_home_page(self):
        self.driver.get("https://bonigarcia.dev/"
                        "selenium-webdriver-java/"
                        "slow-calculator.html")

    def delay_field(self, delay):
        input_field = self.driver.find_element(By.ID, "delay")
        input_field.clear()
        input_field.send_keys(delay)

    def click_submit(self, buttons):
        self.driver.find_element(
            By.CSS_SELECTOR, '[class="clear btn '
                             'btn-outline-danger"]').click()
        for button in buttons:
            self.driver.find_element(
                By.XPATH, f"//span[text()='{button}']").click()

    def screen(self, value):
        wait = WebDriverWait(self.driver, 45, 0.5)
        wait.until(EC.text_to_be_present_in_element(
            (By.CSS_SELECTOR, '[class="screen"]'), str(value)))
        itog = self.driver.find_element(
            By.CSS_SELECTOR, '[class="screen"]')
        ravno = itog.get_attribute("textContent").strip()
        return ravno

    def close(self):
        self.driver.quit()
