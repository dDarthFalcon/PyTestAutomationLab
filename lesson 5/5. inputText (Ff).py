from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

# Инициализация веб-драйвера для Firefox
driver = webdriver.Firefox()

# Открыть страницу
driver.get("http://the-internet.herokuapp.com/inputs")

# Локатор для текстового поля
input_locator = "input[type='number']"
# Найти текстовое поле
input_field = driver.find_element(By.CSS_SELECTOR, input_locator)

# Ввести текст "1000" в поле
input_field.send_keys("1000")
sleep(1)  # Небольшая пауза для наблюдения

# Очистить поле
input_field.clear()
sleep(1)  # Небольшая пауза для наблюдения

# Ввести текст "999" в поле
input_field.send_keys("999")
sleep(1)  # Небольшая пауза для наблюдения

# Закрыть браузер
driver.quit()