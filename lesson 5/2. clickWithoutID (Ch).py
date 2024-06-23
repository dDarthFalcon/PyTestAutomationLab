from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

# Инициализация веб-драйвера для Chrome
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.maximize_window()

def click_dynamic_button(driver):
    # Открыть страницу
    driver.get("https://uitestingplayground.com/dynamicid")
    # Локатор для синей кнопки (предположительно используем класс)
    button_locator = "button.btn.btn-primary"
    # Найти синюю кнопку и кликнуть на нее
    dynamic_button = driver.find_element(By.CSS_SELECTOR, button_locator)
    # Небольшая пауза между итерациями, чтобы наблюдать за процессом
    sleep(1)
    dynamic_button.click()

for _ in range(3):
    click_dynamic_button(driver)
    # Небольшая пауза между итерациями, чтобы наблюдать за процессом
    sleep(1)
    # Закрыть браузер

driver.quit()


