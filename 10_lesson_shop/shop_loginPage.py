from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import allure

@allure.severity("Blocker")
@allure.id("LOG")
@allure.epic("LOG")
@allure.title("Class LOGINPage")
@allure.story("Создание Класса страницы логирования, открытие страницы магазина, ввод login&password, нажатие на кнопку логин")
class LoginPage:
    @allure.title("Инициализация класса LOGINPage")
    def __init__(self, driver):
        """
            создание драйвера, открытия драйвера на весь экран,
            переход на ПЕРВУЮ страницу сайта магазина с логизацией.
        """
        self.driver = driver
        with allure.step("создание общей задержки драйвера на 50 сек."):
            self.wait = WebDriverWait(self.driver, 50)
        with allure.step("увеличение драйвера на весь экран"):
            self.driver.maximize_window()
        with allure.step("это адрес странички логинации"):
            self.driver.get("https://www.saucedemo.com/")

    @allure.title("Ввод {login}:{password}")
    @allure.description("Ввод логина и пароля,это первый степ, данные вводятся на странице теста")
    @allure.epic("LOG")
    def log(self, login: str, password: str):
        """
           Здесь задается функция ввода клавиш
           в поле login и password
           сами данные вносятся через test_shop.py
        """
        with allure.step("Нахождение поля login"):
            self.driver.find_element(
                By.CSS_SELECTOR, '[name="user-name"]').send_keys(login)
        with allure.step("Нахождение поля password"):
            self.driver.find_element(
                By.CSS_SELECTOR, '[name="password"]').send_keys(password)
    @allure.title("Нажатие кнопки Login")
    @allure.description("нажатие на кнопку логизации и переход на следующую страницу shop_mainPage.py")
    @allure.epic("BUTTON")
    def login(self):
        self.driver.find_element(
            By.CSS_SELECTOR, '[name="login-button"]').click()
