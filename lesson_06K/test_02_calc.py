import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


def test_calculator(browser):
    browser.implicitly_wait(10)
    pause = WebDriverWait(browser, 45)
    browser.get(
        "https://bonigarcia.dev/"
        "selenium-webdriver-java/"
        "slow-calculator.html ")

    input_field = browser.find_element(By.ID, "delay")
    input_field.clear()
    input_field.send_keys(45)
# чтобы очистить калькулятор перед вводом цифр
    browser.find_element(
        By.CSS_SELECTOR, '[class="clear btn btn-outline-danger"]').click()
# keys
    buttons = ["7", "+", "8", "="]
    for button, in buttons:
        browser.find_element(
            By.XPATH, f"//span[text()='{button}']").click()

    pause.until(EC.text_to_be_present_in_element(
        (By.CSS_SELECTOR, '[class="screen"]'), "15"))
    itog = browser.find_element(
        By.CSS_SELECTOR, '[class="screen"]')
    ravno = itog.get_attribute("textContent").strip()
    assert ravno == "15"
