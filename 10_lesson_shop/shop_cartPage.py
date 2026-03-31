from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import allure


@allure.severity("Severe")
@allure.id("Button Page")
@allure.epic("BUTTON")
@allure.title("Class CartPage")
@allure.story("Создание класса,"
              " инициализация и нажатие на кнопку Checkout")
class CartPage:
    """
        В этом классе создан драйвер страницы и
        нажатие на кнопку Checkout button
    """

    def __init__(self, driver):
        self.driver = driver
        with allure.step("ожидание драйвера 50 сек"):
            self.wait = WebDriverWait(self.driver, 50)
            self.driver.maximize_window()

    @allure.id("BUTTON")
    @allure.epic("BUTTON")
    @allure.title("кнопка перехода на страницу shop_checkoutPage.py")
    @allure.description("эта функция находит кнопку по ID "
                        "'checkout' и нажимает на кнопку CHECKOUT")
    def checkout(self):
        """
           функция нажатия на кнопку Checkout
        """
        with allure.step("нахождение кнопки по ID и нажатие на нее"):
            self.driver.find_element(
                By.ID, "checkout").click()
