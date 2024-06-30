from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from pages.CalculatorPage import CalculatorPage


def test_slow_calculator():
    browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    calculator_page = CalculatorPage(browser)
    calculator_page.set_delay("45")
    calculator_page.click_button("7")
    calculator_page.click_button("+")
    calculator_page.click_button("8")
    result = calculator_page.get_result()
    assert result == "15"
