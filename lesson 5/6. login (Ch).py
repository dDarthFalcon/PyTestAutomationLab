from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# Инициализация веб-драйвера для Chrome
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# Открыть страницу
driver.get("http://the-internet.herokuapp.com/login")

# Локатор для поля username
username_locator = "input#username"
# Локатор для поля password
password_locator = "input#password"
# Локатор для кнопки Login
login_button_locator = "button.radius"

# Найти поле username и ввести значение "tomsmith"
username_field = driver.find_element(By.CSS_SELECTOR, username_locator)
username_field.send_keys("tomsmith")

# Найти поле password и ввести значение "SuperSecretPassword!"
password_field = driver.find_element(By.CSS_SELECTOR, password_locator)
password_field.send_keys("SuperSecretPassword!")

# Найти кнопку Login и кликнуть на нее
login_button = driver.find_element(By.CSS_SELECTOR, login_button_locator)
login_button.click()

# Небольшая пауза для наблюдения
sleep(2)

# Закрыть браузер
driver.quit()