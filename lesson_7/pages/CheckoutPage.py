from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver
        self.driver.get("https://www.saucedemo.com/checkout-step-one.html")
        self.driver.implicitly_wait(4)

    def fill_checkout_form(self):
        # Вводим данные, которые будут передаваться
        first_name = 'Ivan'
        last_name = 'Petrov'
        postal_code = '123456'
        # Отправляем данные
        self.driver.find_element(By.CSS_SELECTOR,"#first-name").send_keys(first_name)
        self.driver.find_element(By.CSS_SELECTOR, "#last-name").send_keys(last_name)
        self.driver.find_element(By.CSS_SELECTOR, "#postal-code").send_keys(postal_code)

    def go_to_next_step (self):
        # Нажимаем кнопку "Продолжить"
        self.driver.find_element(By.CSS_SELECTOR, "#continue").click()
