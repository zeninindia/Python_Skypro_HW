from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import allure


@allure.epic("Calculator")
@allure.severity("blocker")
@allure.title("создание класса")
@allure.story("создание класса CalculatorPage")
class CalculatorPage:
    @allure.title("инициализация класса")
    @allure.story("определение параметра driver для класса CalculatorPage")
    def __init__(self, driver):
        self.driver = driver

        with allure.step("открытие Chromedriver в размер экрана"):
            self.driver.maximize_window()

    @allure.id("Home_page")
    @allure.story("открытие сайта Slow calculator")
    @allure.title("открытие страницы")
    @allure.feature("GET")
    def open_home_page(self):
        """
            эта функция отвечает за создание драйвера
            подключения к сайту
        """
        # ввод адреса страницы
        with allure.step("определение параметра driver"):
            self.driver.get("https://bonigarcia.dev/"
                        "selenium-webdriver-java/"
                        "slow-calculator.html")

    @allure.id("INPUT DELAY")
    @allure.title("поле задержки")
    @allure.story("нахождения поля ввода 'delay' и ввод данных задержки ")
    @allure.feature("INPUT")
    def delay_field(self, delay: str):
        """
           функция очищает поле ввода калькулятора
           вносит параметр задержки
           выдачи результата калькулятора
           (как в условиях задания)
        """
        # id="delay"
        with allure.step("нахождение поля ввода по локатору ID"):
            input_field = self.driver.find_element(By.ID, "delay")
        with allure.step("очищение поля ввода"):
            input_field.clear()
        # ввод параметра задержки времени в файле test_calculator.py
        with allure.step("заполнения поля 'delay' параметром {delay}"):
            input_field.send_keys(delay)



    @allure.id("CHOSE BUTTONS")
    @allure.title("кнопки")
    @allure.story("очистка, выбор и нажатие кнопок на калькуляторе")
    @allure.feature("SUBMIT")
    def click_submit(self, buttons):
        """
           эта функция очищает поле ввода
           в калькуляторе и нажимает внесенные в
            test_calculator.py кнопки.
        """
        self.driver.find_element(
            By.CSS_SELECTOR, '[class="clear btn '
                             'btn-outline-danger"]').click()

        # ввод параметра кнопок в файле test_calculator.py
        with allure.step("ввод и нажатие кнопок {button}"):
            for button in buttons:
                self.driver.find_element(
                    By.XPATH, f"//span[text()='{button}']").click()

    # ожидание появления результата на экране калькулятора и получения результата в формате строки
    @allure.step("получение результата вычисления калькулятора")
    def screen(self, value):
        wait = WebDriverWait(self.driver, 60, 0.5)
        wait.until(EC.text_to_be_present_in_element(
            (By.CSS_SELECTOR, '[class="screen"]'), str(value)))
        itog = self.driver.find_element(
            By.CSS_SELECTOR, '[class="screen"]')
        ravno = itog.get_attribute("textContent").strip()
        return ravno

    def close(self):
        self.driver.quit()
