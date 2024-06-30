from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self.driver.get("https://www.saucedemo.com/cart.html")
        self.driver.implicitly_wait(4)

    def go_to_checkout (self):
        self.driver.find_element(By.CSS_SELECTOR,"#checkout").click()