from selenium.webdriver.common.by import By
from base.base_page import BasePage


class HomePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    _search_textbox_id = "twotabsearchtextbox"
    _search_button_css = ".nav-search-submit.nav-sprite"
    _inline_banner_id = "gw-desktop-herotator"
    _first_result_base_xpath = "//li[@id='result_0']//a[contains(@title,'{PRODUCT_PLACEHOLDER}')]"

    def getSearchField(self):
        return self.driver.find_element(By.ID, self._search_textbox_id)

    def clickSearchButton(self):
        self.driver.find_element(By.CSS_SELECTOR, self._search_button_css).click()

    def searchFor(self, product):
        self.getSearchField().send_keys(product)
        self.clickSearchButton()

    def clickInlineBanner(self):
        self.driver.find_element(By.ID, self._inline_banner_id).click()

    def verifySearchResult(self, product):
        first_result_xpath = self._first_result_base_xpath.format(PRODUCT_PLACEHOLDER = product)
        return self.isElementPresent(first_result_xpath, "xpath")

