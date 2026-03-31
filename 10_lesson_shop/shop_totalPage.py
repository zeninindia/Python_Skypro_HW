import re
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import allure


@allure.severity("Blocker")
@allure.id("TOTAL")
@allure.epic("TOTAL")
@allure.title("Class Total")
@allure.story("Создание класса страницы ИТОГ и "
              "выведение суммы заказа в терминал")
class TotalPage:
    """
       на этой странице отображается итоговая сумма
       здесь находятся функции вывода итоговой суммы
       и проверка соответствия ожидания и результата
    """

    @allure.title("Инициализация класса TotalPage")
    @allure.id("INIT")
    def __init__(self, driver):
        with allure.step("создание драйвера класса"):
            self.driver = driver
        with allure.step("время ожидание драйвера 50 сек."):
            self.wait = WebDriverWait(self.driver, 50)
            self.summ = None

    @allure.title("Вывод итога")
    @allure.description("Ввод итога заказа и сравнение"
                        " с ожидаемым результатам")
    @allure.epic("TOTAL")
    def total_page(self):
        """
           ожидание появление результата на странице
           выявление цифры суммы
           печать суммы в консоль и сравнение
        """
        with allure.step("ожидание появление итога в поле Total"):
            total_element = self.wait.until(
                EC.presence_of_element_located((
                    By.CSS_SELECTOR, '[class="summary_total_label"]')))
        with allure.step("выявление цифровой суммы итога"):
            total = total_element.get_attribute("textContent").strip()
        with allure.step("печать итога в консоль"):
            print(total)
        nums = re.search(r'\$(\d+\.\d{2})', total)
        summ = float(nums.group(1))
        with allure.step("возвращает в функцию цифру"
                         " отображенную в поле суммы"):
            return summ
