from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

from config.config import (
    STORE_PASSWORD,
    BASE_URL,
    PRODUCT_NAME
)

from pages.login_page import LoginPage
from pages.home_page import HomePage
from pages.product_page import ProductPage
from pages.cart_page import CartPage


def test_add_product_to_cart():

    # Chrome options
    options = Options()

    options.page_load_strategy = "eager"

    # Launch browser
    driver = webdriver.Chrome(
        service=Service(
            ChromeDriverManager().install()
        ),
        options=options
    )

    driver.maximize_window()

    # Open website
    driver.get(BASE_URL)

    # Create page objects
    login = LoginPage(driver)

    home = HomePage(driver)

    product = ProductPage(driver)

    cart = CartPage(driver)

    try:

        # Login
        login.enter_password(STORE_PASSWORD)

        login.click_enter_button()

        # Search product
        home.click_search_icon()

        home.search_product(PRODUCT_NAME)

        # Select product
        home.select_product()

        # Add to cart
        product.add_product_to_cart()

        # Open cart
        cart.open_cart()

        # Verify product
        cart.verify_product_in_cart()

    finally:

        driver.quit()


if __name__ == "__main__":

    test_add_product_to_cart()