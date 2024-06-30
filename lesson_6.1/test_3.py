import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture
def driver():
    # Инициализация веб-драйвера для Chrome
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.implicitly_wait(4)
    yield driver
    driver.quit()

def test_purchase(driver):
    # Открыть страницу магазина
    driver.get("https://www.saucedemo.com/")
    
    # Авторизация
    driver.find_element(By.CSS_SELECTOR, "#user-name").send_keys("standard_user")
    driver.find_element(By.CSS_SELECTOR, "#password").send_keys("secret_sauce")
    driver.find_element(By.CSS_SELECTOR, "#login-button").click()

    # Добавление товаров в корзину
    items_to_add = [
        "#add-to-cart-sauce-labs-backpack",
        "#add-to-cart-sauce-labs-bolt-t-shirt",
        "#add-to-cart-sauce-labs-onesie"
    ]
    
    for item_id in items_to_add:
        driver.find_element(By.CSS_SELECTOR, item_id).click()

    # Перейти в корзину
    driver.find_element(By.CSS_SELECTOR, "#shopping_cart_container").click()

    # Нажать Checkout
    driver.find_element(By.CSS_SELECTOR, "#checkout").click()

    # Заполнение формы
    driver.find_element(By.CSS_SELECTOR, "#first-name").send_keys("Иван")
    driver.find_element(By.CSS_SELECTOR, "#last-name").send_keys("Петров")
    driver.find_element(By.CSS_SELECTOR, "#postal-code").send_keys("123456")
    driver.find_element(By.CSS_SELECTOR, "#continue").click()

    # Получение и проверка итоговой стоимости
    total_element = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".summary_total_label"))
    )
    total_text = total_element.text
    assert total_text == "Total: $58.29"
