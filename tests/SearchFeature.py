from selenium import webdriver
from selenium.webdriver.common.by import By

class SearchTest():

    def test_validSearch(self):
        baseURL = "http://www.amazon.com"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.implicitly_wait(3)

        driver.get(baseURL)

        driver.find_element(By.ID, "twotabsearchtextbox").send_keys("Echo Show")
        driver.find_element(By.XPATH, "//div[@class='nav-search-submit nav-sprite']/input").click()
        driver.close()

test = SearchTest()
test.test_validSearch()