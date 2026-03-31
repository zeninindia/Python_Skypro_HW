from selenium.webdriver.common.by import By
import allure


@allure.severity("Blocker")
@allure.id("LOG")
@allure.epic("LOG")
@allure.title("Class LOGINPage2 для доставки ")
@allure.story("ввод данных для доставки, "
              "нажатие на кнопку continue переход на страницу "
              "shop_totalPage.py")
class CheckoutPage:
    """
       создание класса страницы ввода данных для доставки
    """

    def __init__(self, driver):
        self.driver = driver
        self.driver.implicitly_wait(5)
        # self.wait = WebDriverWait(self.driver, 50)

    @allure.severity("Blocker")
    @allure.id("LOG")
    @allure.epic("LOG")
    @allure.title("Class LOGINPage2 для доставки ")
    @allure.story("ввод данных для доставки, "
                  "нажатие на кнопку continue переход на страницу "
                  "shop_totalPage.py")
    def name_fields(self, f_name: str, l_name: str, zipp: int):
        """
           в этой функции нахождение полей и заполнение их,
           а сами данные вносятся на странице test_shop.py
        """
        with allure.step("нахождение поля ввода имени first name "
                         "{f_name}"):
            self.driver.find_element(
                By.ID, "first-name").send_keys(f_name)
        with allure.step("нахождение поля ввода фамилии last name"
                         " {l_name}"):
            self.driver.find_element(
                By.ID, "last-name").send_keys(l_name)
        with allure.step("нахождение поля ввода почтовый индекс postal code "
                         "{zipp}"):
            self.driver.find_element(
                By.ID, "postal-code").send_keys(zipp)

    @allure.id("BUTTON")
    @allure.epic("BUTTON")
    @allure.title("кнопка перехода на страницу shop_totalPage.py")
    @allure.description("эта функция находит "
                        "кнопку и нажимает на кнопку CONTINUE")
    def cont(self):
        """
           функция нажатия на кнопку Continue
        """
        with allure.step("нахождение кнопки по"
                         " CSS_SELECTOR и нажатие на нее"):
            self.driver.find_element(
                By.CSS_SELECTOR, '[name="continue"]').click()
