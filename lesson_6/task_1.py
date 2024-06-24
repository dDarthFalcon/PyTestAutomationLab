from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Инициализация веб-драйвера для Chrome
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# Открыть страницу
driver.get("http://uitestingplayground.com/ajax")

# Локатор для синей кнопки
button_locator = "button#ajaxButton"

# Найти синюю кнопку и кликнуть на нее
blue_button = driver.find_element(By.CSS_SELECTOR, button_locator)
blue_button.click()

# Локатор для зеленой плашки
message_locator = "div#content p.bg-success"

# Ожидать появления зеленой плашки и получения текста
WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, message_locator)))
message_element = driver.find_element(By.CSS_SELECTOR, message_locator)
message_text = message_element.text

# Вывести текст в консоль
print(message_text)

# Закрыть браузер
driver.quit()
