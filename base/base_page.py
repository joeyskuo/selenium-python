from selenium.webdriver.common.by import By

class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def isElementPresent(self, locator, locatorType="id"):
        try:
            if locatorType == "id":
                element = self.driver.find_element(By.ID, locator)
            elif locatorType == "xpath":
                element = self.driver.find_element(By.XPATH, locator)
            else:
                print("locatorType " + locatorType + " not supported.")
                return None
        except:
            return False
        return True