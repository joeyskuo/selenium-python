from selenium import webdriver
from selenium.webdriver.common.by import By

class BannerTest():

    def test_addToCart(self):
        baseURL = "http://www.amazon.com"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.implicitly_wait(3)

        driver.get(baseURL)

        driver.find_element(By.ID, "gw-desktop-herotator").click()
        driver.find_element(By.ID, "add-to-cart-button").click()

        driver.close()

test = BannerTest()
test.test_addToCart()