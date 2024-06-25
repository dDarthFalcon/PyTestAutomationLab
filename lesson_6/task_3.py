from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Инициализация веб-драйвера для Chrome
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# Открыть страницу
driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")

# Локатор для текста "Done"
done_text_locator = "#text"

# Явное ожидание появления текста "Done"
WebDriverWait(driver, 40).until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, done_text_locator), "Done")
)

# Найти 3-ю картинку
images = driver.find_elements(By.CSS_SELECTOR, "#image-container img")

# Получить значение атрибута 'src' у 3-й картинки
src_value = images[2].get_attribute("src")

# Вывести значение в консоль
print(src_value)

# Закрыть браузер
driver.quit()