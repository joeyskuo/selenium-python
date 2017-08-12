from selenium.webdriver.common.by import By

class ProductPage:

    def __init__(self, driver):
        self.driver = driver

    # Locators
    _add_to_cart_button_id = "add-to-cart-button"
    _added_to_cart_text_id = "confirm-text"

    def clickAddToCartButton(self):
        self.driver.find_element(By.ID, self._add_to_cart_button_id).click()

    def verifyAddToCartSuccessful(self):
        return self.isElementPresent(self._added_to_cart_text_id)

    def isElementPresent(self, locator, locatorType="id"):
        try:
            element = self.driver.find_element(By.ID, locator)
        except:
            return False
        return True