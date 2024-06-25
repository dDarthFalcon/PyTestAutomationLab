import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def driver():
    # Инициализация веб-драйвера для Chrome
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    yield driver
    driver.quit()

def test_slow_calculator(driver):
    # Открыть страницу
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    # Ввести значение 45 в поле #delay
    delay_input = driver.find_element(By.CSS_SELECTOR, "#delay")
    delay_input.clear()
    delay_input.send_keys("45")

    # Нажать на кнопки 7 + 8 =
    driver.find_element(By.CSS_SELECTOR, ".keys span:nth-child(1)").click()
    driver.find_element(By.CSS_SELECTOR, ".keys span:nth-child(4)").click()
    driver.find_element(By.CSS_SELECTOR, ".keys span:nth-child(2)").click()
    driver.find_element(By.CSS_SELECTOR, ".keys span:nth-child(15)").click()
    
    # Явное ожидание результата "15" через 45 секунд
    WebDriverWait(driver, 50).until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR, "div.screen"), "15")
    )

    # Проверка результата
    result = driver.find_element(By.CSS_SELECTOR, "div.screen").text
    assert result == "15"
