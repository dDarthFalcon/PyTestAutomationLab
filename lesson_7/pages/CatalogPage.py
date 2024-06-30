from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

class CatalogPage:
    def __init__(self, driver):
        self.driver = driver
        self.driver.get("https://www.saucedemo.com/inventory.html")
        self.driver.implicitly_wait(4)
        self.items = {
            "backpack": (By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack"),
            "tshirt": (By.CSS_SELECTOR, "#add-to-cart-sauce-labs-bolt-t-shirt"),
            "onesie": (By.CSS_SELECTOR, "#add-to-cart-sauce-labs-onesie")
        }

    def add_to_cart(self,item):
        self.driver.find_element(*self.items[item]).click()

    def go_to_cart(self):
        self.driver.get("https://www.saucedemo.com/cart.html")

