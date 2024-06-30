from selenium.webdriver.common.by import By

class FormPage:
    def __init__(self, driver):
        self.driver = driver
        self.driver.get('https://bonigarcia.dev/selenium-webdriver-java/data-types.html')
        self.driver.implicitly_wait(4)

    def fill_form(self):
        first_name = 'Иван'
        last_name = 'Петров'
        address = 'Ленина, 55-3'
        city = 'Москва'
        country = 'Россия'
        zipcode = ''
        email = 'test@skypro.com'
        phone = '+7985899998787'
        job_position = 'QA'
        company = 'SkyPro'
        self.driver.find_element(By.CSS_SELECTOR, "input[name='first-name']").send_keys(first_name)
        self.driver.find_element(By.CSS_SELECTOR, "input[name='last-name']").send_keys(last_name)
        self.driver.find_element(By.CSS_SELECTOR, "input[name='address']").send_keys(address)
        self.driver.find_element(By.CSS_SELECTOR, "input[name='zip-code']").send_keys(zipcode)
        self.driver.find_element(By.CSS_SELECTOR, "input[name='e-mail']").send_keys(email)
        self.driver.find_element(By.CSS_SELECTOR, "input[name='phone']").send_keys(phone)
        self.driver.find_element(By.CSS_SELECTOR, "input[name='city']").send_keys(city)
        self.driver.find_element(By.CSS_SELECTOR, "input[name='country']").send_keys(country)
        self.driver.find_element(By.CSS_SELECTOR, "input[name='job-position']").send_keys(job_position)
        self.driver.find_element(By.CSS_SELECTOR, "input[name='company']").send_keys(company)

    def submit_form(self):
        self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    def get_blank_fields(self):
        fill_form = self.driver.find_elements(By.CSS_SELECTOR,".alert-danger")
        blank_fields_id = []
        for field in fill_form:
            blank_field_id = field.get_attribute("id")
            blank_fields_id.append(blank_field_id)
        return blank_fields_id

    def get_fill_fields(self):
        fill_form = self.driver.find_elements(By.CSS_SELECTOR,".alert-success")
        fill_fields_id = []
        for field in fill_form:
            fill_field = field.get_attribute("id")
            fill_fields_id.append(fill_field)
        return fill_fields_id
