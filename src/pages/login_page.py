from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:

    def __init__(self, driver):

        self.driver = driver

        self.wait = WebDriverWait(driver, 20)

    PASSWORD_FIELD = (By.NAME, "password")

    ENTER_BUTTON = (
        By.CSS_SELECTOR,
        "button[type='submit']"
    )

    def enter_password(self, password):

        password_field = self.wait.until(
            EC.visibility_of_element_located(
                self.PASSWORD_FIELD
            )
        )

        password_field.send_keys(password)

    def click_enter_button(self):

        enter_button = self.wait.until(
            EC.element_to_be_clickable(
                self.ENTER_BUTTON
            )
        )

        enter_button.click()