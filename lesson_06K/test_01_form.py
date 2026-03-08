from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def test_input_fields():
    driver = webdriver.Edge()
    driver.maximize_window()

    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
    driver.execute_script("document.body.style.zoom='70%'")

    fields = {
        "first-name": "Иван",
        "last-name": "Петров",
        "address": "Ленина, 55-3",
        "e-mail": "test@skypro.com",
        "phone": "+7985899998787",
        "city": "Москва",
        "country": "Россия",
        "job-position": "QA",
        "company": "SkyPro"
    }
    for field, value in fields.items():
        driver.find_element(By.NAME, field).send_keys(value)

    driver.find_element(By.CSS_SELECTOR, '[type="submit"]').click()

    pause = WebDriverWait(driver, 10)
    pause.until(
        EC.visibility_of_element_located((By.ID, 'zip-code')))
    zip_code = driver.find_element(
        By.ID, 'zip-code').value_of_css_property('background-color')
    assert zip_code == 'rgba(248, 215, 218, 1)', "Поле должно быть красным"

    for field in fields.keys():
        field_color = driver.find_element(
            By.ID, field).value_of_css_property('background-color')
        assert field_color == 'rgba(209, 231, 221, 1)'

    driver.quit()
