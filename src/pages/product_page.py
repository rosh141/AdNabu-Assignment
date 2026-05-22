from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ProductPage:

    def __init__(self, driver):

        self.driver = driver

        self.wait = WebDriverWait(driver, 20)

    ADD_TO_CART_BUTTON = (
        By.NAME,
        "add"
    )

    def add_product_to_cart(self):

        add_to_cart_button = self.wait.until(
            EC.element_to_be_clickable(
                self.ADD_TO_CART_BUTTON
            )
        )

        add_to_cart_button.click()