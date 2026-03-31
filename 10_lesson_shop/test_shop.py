from selenium import webdriver
from shop_loginPage import LoginPage
from shop_mainPage import MainPage
from shop_cartPage import CartPage
from shop_checkoutPage import CheckoutPage
from shop_totalPage import TotalPage
import allure


@allure.severity("Blocker")
@allure.id("shop")
@allure.epic("shop")
@allure.story("проверка работы сайта shop")
def test_checkout():
    """
       функция регистрации {lp}, корзины {mp} и заказа {cp} и получение итога {tp}
    """
    with allure.step("открытие страницы Firefox"):
        driver = webdriver.Firefox()
    with allure.step("определение драйвера со страницы LoginPage"):
        lp = LoginPage(driver)
    with allure.step("регистрация на странице Login Page, ввод {login}:{password}"):
        lp.log("standard_user", "secret_sauce")
    with allure.step("нажатие на кнопку Login"):
        lp.login()

    with allure.step("определение драйвера со страницы MainPage"):
        mp = MainPage(driver)
    with allure.step("выбор конкретных кнопок из списка element на странице mainPage"):
        mp.choose_items("Backpack")
    mp.choose_items("T-Shirt")
    mp.choose_items("Onesie")
    with allure.step("нажатие на кнопку корзины"):
        mp.cart()

    with allure.step("определение драйвера со страницы CartPage"):
        crdp = CartPage(driver)
    with allure.step("нажатие на кнопку Checkout"):
        crdp.checkout()

    with allure.step("определение драйвера со страницы CheckoutPage"):
        cp = CheckoutPage(driver)
    with allure.step("функция заполнения полей доставки, ввод данных {f_name}:{l_name}:{zipp}"):
        cp.name_fields("Olga", "Зенкина", "123456")
    with allure.step("нажатие на кнопку Continue"):
        cp.cont()

    with allure.step("определение драйвера со страницы TotalPage"):
        tp = TotalPage(driver)
    with allure.step("выявление итога и превращение его в цифры"):
        up = tp.total_page()
    with allure.step("проверка соответствия итога ожидаемому результатау"):
        assert up == 58.29

    driver.quit()
