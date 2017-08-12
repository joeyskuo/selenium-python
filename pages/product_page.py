from selenium.webdriver.common.by import By
from base.base_page import BasePage

class ProductPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    _add_to_cart_button_id = "add-to-cart-button"
    _added_to_cart_text_id = "confirm-text"

    def clickAddToCartButton(self):
        self.driver.find_element(By.ID, self._add_to_cart_button_id).click()

    def verifyAddToCartSuccessful(self):
        return self.isElementPresent(self._added_to_cart_text_id)
