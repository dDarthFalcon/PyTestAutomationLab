from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from pages.FormPage import FormPage

def test_fill_form():
    browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    form_page = FormPage(browser)
    form_page.fill_form()
    form_page.submit_form()
    fill_fields = form_page.get_fill_fields()
    expected_fields = ['first-name', 'last-name', 'address', 'city', 'country', 'e-mail', 'phone', 'job-position', 'company']
    assert all(field in fill_fields for field in expected_fields)

def test_blank_form():
    browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    form_page = FormPage(browser)
    form_page.fill_form()
    form_page.submit_form()
    blank_fields = form_page.get_blank_fields()
    expected_fields = ["zip-code"]
    assert all(field in blank_fields for field in expected_fields)