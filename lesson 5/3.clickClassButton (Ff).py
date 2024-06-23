from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Инициализация веб-драйвера для Firefox
driver = webdriver.Firefox()

def click_class_button(driver):
    # Открыть страницу
    driver.get("http://uitestingplayground.com/classattr")
    # Локатор для синей кнопки (по CSS-классу)
    button_locator = ".btn-primary"
    # Найти синюю кнопку и кликнуть на нее
    class_button = driver.find_element(By.CSS_SELECTOR, button_locator)
    class_button.click()
    sleep(2)
    # Обработать всплывающее окно (alert)
    alert = driver.switch_to.alert
    alert.accept()
  
for _ in range(3):
    click_class_button(driver)
    # Небольшая пауза между итерациями, чтобы наблюдать за процессом
    sleep(1)

driver.quit()
