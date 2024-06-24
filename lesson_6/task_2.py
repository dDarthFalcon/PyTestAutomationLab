from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Инициализация веб-драйвера для Chrome
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# Открыть страницу
driver.get("http://uitestingplayground.com/textinput")

# Локатор для поля ввода
input_locator = "input#newButtonName"
# Локатор для синей кнопки
button_locator = "button#updatingButton"

# Найти поле ввода и ввести текст "SkyPro"
input_field = WebDriverWait(driver, 4).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, input_locator))
)
input_field.send_keys("SkyPro")

# Найти синюю кнопку и кликнуть на нее
driver.find_element(By.CSS_SELECTOR, button_locator).click()

# Ожидать, пока текст кнопки изменится на "SkyPro"
WebDriverWait(driver, 4).until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, button_locator), "SkyPro")
)

# Получить текст кнопки
button_text = driver.find_element(By.CSS_SELECTOR, button_locator).text

# Вывести текст в консоль
print(button_text)

# Закрыть браузер
driver.quit()