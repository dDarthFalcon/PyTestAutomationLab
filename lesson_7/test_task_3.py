from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from pages.LoginPage import LoginPage
from pages.CatalogPage import CatalogPage
from pages.CartPage import CartPage
from pages.CheckoutPage import CheckoutPage
from pages.OverviewPage import OverviewPage

def test_sum():
    browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    login_page = LoginPage(browser)
    login_page.login()

    catalog_page = CatalogPage(browser)
    catalog_page.add_to_cart("backpack")
    catalog_page.add_to_cart("tshirt")
    catalog_page.add_to_cart("onesie")   
    catalog_page.go_to_cart()

    cart_page = CartPage(browser)
    cart_page.go_to_checkout()

    Checkout_page = CheckoutPage(browser)
    Checkout_page.fill_checkout_form()
    Checkout_page.go_to_next_step()

    overview_page = OverviewPage(browser)
    cart_price = overview_page.get_total()
    assert cart_price == "Total: $58.29"
