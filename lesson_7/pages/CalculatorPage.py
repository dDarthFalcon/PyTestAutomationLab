from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CalculatorPage:
    def __init__(self, driver):
        self.driver = driver
        self.driver.get('https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html')
        self.driver.implicitly_wait(4)
        self.buttons = {
            "7": (By.CSS_SELECTOR, ".keys span:nth-child(1)"),
            "8": (By.CSS_SELECTOR, ".keys span:nth-child(2)"),
            "9": (By.CSS_SELECTOR, ".keys span:nth-child(3)"),
            "+": (By.CSS_SELECTOR, ".keys span:nth-child(4)"),
            "4": (By.CSS_SELECTOR, ".keys span:nth-child(5)"),
            "5": (By.CSS_SELECTOR, ".keys span:nth-child(6)"),
            "6": (By.CSS_SELECTOR, ".keys span:nth-child(7)"),
            "-": (By.CSS_SELECTOR, ".keys span:nth-child(8)"),
            "1": (By.CSS_SELECTOR, ".keys span:nth-child(9)"),
            "2": (By.CSS_SELECTOR, ".keys span:nth-child(10)"),
            "3": (By.CSS_SELECTOR, ".keys span:nth-child(11)"),
            "/": (By.CSS_SELECTOR, ".keys span:nth-child(12)"),
            "0": (By.CSS_SELECTOR, ".keys span:nth-child(13)"),
            ".": (By.CSS_SELECTOR, ".keys span:nth-child(14)"),
            "=": (By.CSS_SELECTOR, ".keys span:nth-child(15)"),
            "*": (By.CSS_SELECTOR, ".keys span:nth-child(16)"),
        }

    def set_delay(self, delay):
        delay_input = self.driver.find_element(By.CSS_SELECTOR, "#delay")
        delay_input.clear()
        delay_input.send_keys(delay)

    def click_button(self, button):
        self.driver.find_element(*self.buttons[button]).click()

    def get_result(self):
        self.driver.find_element(By.CSS_SELECTOR,".keys span:nth-child(15)").click()
        WebDriverWait(self.driver, 50).until(
            EC.text_to_be_present_in_element((By.CSS_SELECTOR, "div.screen"), "15")
        )
        return self.driver.find_element(By.CSS_SELECTOR, "div.screen").text
