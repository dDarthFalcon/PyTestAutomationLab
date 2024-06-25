import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture
def driver():
    # Инициализация веб-драйвера для Chrome
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    yield driver
    driver.quit()

def test_form_submission(driver):
    driver.get('https://bonigarcia.dev/selenium-webdriver-java/data-types.html')

    # Задаем значение CSS селекторов
    first_name = "input[name='first-name']"
    last_name = "input[name='last-name']"
    address = "input[name='address']"
    email = "input[name='e-mail']"
    phone = "input[name='phone']"
    city = "input[name='city']"
    country = "input[name='country']"
    job_position = "input[name='job-position']"
    company = "input[name='company']"

    # Заполнение формы
    driver.find_element(By.CSS_SELECTOR, first_name).send_keys('Иван')
    driver.find_element(By.CSS_SELECTOR, last_name).send_keys('Петров')
    driver.find_element(By.CSS_SELECTOR, address).send_keys('Ленина, 55-3')
    driver.find_element(By.CSS_SELECTOR, email).send_keys('test@skypro.com')
    driver.find_element(By.CSS_SELECTOR, phone).send_keys('+7985899998787')
    driver.find_element(By.CSS_SELECTOR, city).send_keys('Москва')
    driver.find_element(By.CSS_SELECTOR, country).send_keys('Россия')
    driver.find_element(By.CSS_SELECTOR, job_position).send_keys('QA')
    driver.find_element(By.CSS_SELECTOR, company).send_keys('SkyPro')

    # Нажатие кнопки Submit
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    # Ожидание, чтобы страница успела обновиться
    driver.implicitly_wait(4)

    # Проверить, что поле Zip code подсвечено красным
    zip_code_field = driver.find_element(By.CSS_SELECTOR, "#zip-code")
    assert "alert-danger" in zip_code_field.get_attribute("class")

    # Проверить, что остальные поля подсвечены зеленым
    fields_to_check = ["#first-name", "#last-name", "#address", 
                       "#e-mail", "#phone", "#city", 
                       "#country", "#job-position", "#company"]
    for field in fields_to_check:
        input_field = driver.find_element(By.CSS_SELECTOR, field)
        assert "alert-success" in input_field.get_attribute("class")
