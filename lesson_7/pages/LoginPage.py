from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.driver.get("https://www.saucedemo.com/")
        self.driver.implicitly_wait(4)

    def login(self):
        self.driver.find_element(By.CSS_SELECTOR,"#user-name").send_keys("standard_user")
        self.driver.find_element(By.CSS_SELECTOR,"#password").send_keys("secret_sauce")
        self.driver.find_element(By.CSS_SELECTOR,"#login-button").click()