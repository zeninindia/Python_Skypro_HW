from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import allure


@allure.severity("Severe")
@allure.id("SOPPING")
@allure.epic("SOPPING")
@allure.title("Class ShopPage")
@allure.story("Создание класса главной страницы магазина, "
              "выбор товаров и переход в корзину"
              " нажатием на корзину")
class MainPage:
    """
       На этой странице в списке перечислены
       товары, и нажатие на кнопку выбора товара, а сам
       товар выбирается на странице test_shop.py
    """

    @allure.title("Инициализация класса")
    @allure.id("init_class")
    @allure.epic("driver")
    @allure.description("инициализация класса,"
                        " создание драйвера класса, "
                        "ожидание драйвера 50 сек.")
    def __init__(self, driver):
        self.driver = driver
        with allure.step("время открытия драйвера 50 сек."):
            self.wait = WebDriverWait(self.driver, 50)

    @allure.id("BUTTON")
    @allure.epic("BUTTON")
    @allure.title("Список элементов для выбора в корзину")
    @allure.description("здесь записан список элементов"
                        " и прописана функция нажатия кнопки"
                        " 'в корзину'")
    def choose_items(self, element):
        """
           Это список всех возможных
           или необходимых кнопок добавления в корзину
           список elements
        """
        elements = {
            "Backpack": "add-to-cart-sauce-labs-backpack",
            "T-Shirt": "add-to-cart-sauce-labs-bolt-t-shirt",
            "Onesie": "add-to-cart-sauce-labs-onesie",
        }
        with allure.step("эта функция нажимает кнопку "
                         "или кнопки выбранные в test_shop.py"):
            if element in elements:
                self.driver.find_element(
                    By.NAME, elements[element]).click()

    @allure.id("BUTTON")
    @allure.epic("BUTTON")
    @allure.title("кнопка перехода на страницу shop_cartPage.py")
    @allure.description("эта функция нажимает находит кнопку"
                        " по CSS_SELECTOR, '.shopping_cart_link'"
                        "и нажимает на кнопку корзины")
    def cart(self):
        self.driver.find_element(
            By.CSS_SELECTOR, '.shopping_cart_link').click()
