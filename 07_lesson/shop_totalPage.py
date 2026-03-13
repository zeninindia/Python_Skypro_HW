import re
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class TotalPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 50)
        self.summ = None

    def total_page(self):
        total_element = self.wait.until(
            EC.presence_of_element_located((
                By.CSS_SELECTOR, '[class="summary_total_label"]')))
        total = total_element.get_attribute("textContent").strip()
        print(total)
        nums = re.search(r'\$(\d+\.\d{2})', total)
        summ = float(nums.group(1))
        return summ
