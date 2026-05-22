from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CartPage:

    def __init__(self, driver):

        self.driver = driver

        self.wait = WebDriverWait(driver, 20)

    CART_ICON = (
        By.ID,
        "cart-icon-bubble"
    )

    CART_PRODUCT = (
        By.CSS_SELECTOR,
        ".cart-item__name"
    )

    def open_cart(self):

        cart_link = self.wait.until(
            EC.element_to_be_clickable(
                self.CART_ICON
            )
        )

        cart_link.click()

        print("Shopping cart opened successfully.")

    def verify_product_in_cart(self):

        cart_title = self.wait.until(
            EC.visibility_of_element_located(
                self.CART_PRODUCT
            )
        )

        assert cart_title.is_displayed()

        print("Product added successfully to cart.")