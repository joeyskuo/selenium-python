from selenium.webdriver.common.by import By

class HomePage:

    def __init__(self, driver):
        self.driver = driver

    def searchFor(self, product):
        self.driver.find_element(By.ID, "twotabsearchtextbox").send_keys(product)
        self.driver.find_element(By.XPATH, "//div[@class='nav-search-submit nav-sprite']/input").click()