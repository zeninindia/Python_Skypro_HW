from selenium import webdriver
from calculator_page import CalculatorPage


def test_calculator():
    driver = webdriver.Chrome()
    calculator = CalculatorPage(driver)
    calculator.open_home_page()
    calculator.delay_field("45")
    calculator.click_submit(["7", "+", "8", "="])
    res = calculator.screen('15')
    to_be = '15'
    assert res == to_be
    calculator.close()
