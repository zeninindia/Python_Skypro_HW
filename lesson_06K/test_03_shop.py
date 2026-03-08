import re
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


@pytest.fixture
def browser():
    driver = webdriver.Firefox()
    driver.maximize_window()
    yield driver
    driver.quit()


def test_shop(browser):
    browser.implicitly_wait(10)
    pause = WebDriverWait(browser, 5, 0.1)
    browser.get("https://www.saucedemo.com/")

    browser.find_element(
        By.CSS_SELECTOR, '[name="user-name"]').send_keys("standard_user")
    browser.find_element(
        By.CSS_SELECTOR, '[name="password"]').send_keys("secret_sauce")
    browser.find_element(
        By.CSS_SELECTOR, '[name="login-button"]').click()

    browser.find_element(
        By.CSS_SELECTOR, '[name="add-to-cart-sauce-labs-backpack"]').click()
    browser.find_element(
        By.CSS_SELECTOR, '['
                         'name="add-to-cart-sauce-labs-bolt-t-shirt"]').click()
    browser.find_element(
        By.CSS_SELECTOR, '[name="add-to-cart-sauce-labs-onesie"]').click()
    browser.find_element(
        By.CSS_SELECTOR, '.shopping_cart_link').click()

    browser.execute_script(
        "document.body.style.zoom='70%'")

    browser.find_element(
        By.CSS_SELECTOR, '[name="checkout"]').click()

    fields = {
        "firstName": "Olga",
        "lastName": "Zenkina",
        "postalCode": "12345"
    }
    for field, value in fields.items():
        browser.find_element(By.NAME, field).send_keys(value)

    browser.find_element(
        By.CSS_SELECTOR, '[name="continue"]').click()

    total_element = pause.until(
        EC.presence_of_element_located((
            By.CSS_SELECTOR, '[class="summary_total_label"]')))
    total = total_element.get_attribute("textContent").strip()
    print(total)
    nums = re.search(r'\$(\d+\.\d{2})', total)
    assert float(nums.group(1)) == 58.29
