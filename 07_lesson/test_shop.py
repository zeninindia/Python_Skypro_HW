from selenium import webdriver
from shop_loginPage import LoginPage
from shop_mainPage import MainPage
from shop_cartPage import CartPage
from shop_checkoutPage import CheckoutPage
from shop_totalPage import TotalPage


def test_checkout():
    driver = webdriver.Firefox()
    lp = LoginPage(driver)
    lp.log("standard_user", "secret_sauce")
    lp.login()

    mp = MainPage(driver)
    mp.choose_items("Backpack")
    mp.choose_items("T-Shirt")
    mp.choose_items("Onesie")
    mp.cart()

    crdp = CartPage(driver)
    crdp.checkout()

    cp = CheckoutPage(driver)
    cp.name_fields("Olga", "Зенкина", "123456")
    cp.cont()

    tp = TotalPage(driver)
    up = tp.total_page()
    assert up == 58.29

    driver.quit()
