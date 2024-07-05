from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from pages.FormPage import FormPage

# Данные формы
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


def test_fill_form():
    browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    form_page = FormPage(browser)
    form_page.fill_form(first_name, last_name, address, city, country, zipcode, email, phone, job_position, company)
    form_page.submit_form()
    fill_fields = form_page.get_fill_fields()
    expected_fields = ['first-name', 'last-name', 'address', 'city', 'country', 'e-mail', 'phone', 'job-position', 'company']
    assert all(field in fill_fields for field in expected_fields)

def test_blank_form():
    browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    form_page = FormPage(browser)
    form_page.fill_form(first_name, last_name, address, city, country, zipcode, email, phone, job_position, company)
    form_page.submit_form()
    blank_fields = form_page.get_blank_fields()
    expected_fields = ["zip-code"]
    assert all(field in blank_fields for field in expected_fields)
