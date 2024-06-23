from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

# Инициализация веб-драйвера для Firefox
driver = webdriver.Firefox()

# Открыть страницу
driver.get("http://the-internet.herokuapp.com/entry_ad")
# Небольшая пауза, чтобы модальное окно успело появиться
sleep(2)
    
# Локатор для кнопки "Close"
close_button_locator = "div.modal-footer > p"

# Найти кнопку "Close" и кликнуть на нее
close_button = driver.find_element(By.CSS_SELECTOR, close_button_locator)
close_button.click()

# Небольшая пауза, чтобы убедиться, что окно закрылось
sleep(2)

# Закрыть браузер
driver.quit()