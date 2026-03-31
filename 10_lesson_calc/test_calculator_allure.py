from selenium import webdriver
from calculator_page_allure import CalculatorPage
import allure


@allure.severity("Blocker")
@allure.id("test_calculator")
@allure.epic("Calculator")
@allure.story("проверка работы сайта Slow Calculator")
def test_calculator():
    with allure.step("создание драйвера для открытия Chrome Browser"):
        driver = webdriver.Chrome()
    with allure.step("объединение класса CalculatorPage с тестовым файлом"):
        calculator = CalculatorPage(driver)
    with allure.step("открытие сайта Slow Calculator"):
        calculator.open_home_page()
    with allure.step("вызова функции заполнения поля 'delay'"):
        with allure.step("ввод временно`го параметра в строку 'delay' в формате str {delay}"):
            calculator.delay_field("45")
    with allure.step("вызова функции нажатие на кнопки 'keys'"):
        with allure.step("ввод числового параметра для нажатия конкретных кнопок"):
            calculator.click_submit(["7", "+", "8", "="])
    with allure.step("ожидание получения результата на экране калькулятора"):
        res = calculator.screen('15')
    with allure.step("создание переменной для ввода ожидаемого результата"):
        to_be = '15'
    with allure.step("сравнить фактический результат с экрана калькулятора с переменной ожидаемого результата"):
        assert res == to_be
    with allure.step("закрыть все"):
        calculator.close()
