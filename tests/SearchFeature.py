from selenium import webdriver
from pages.home_page import HomePage
import unittest

class SearchTest(unittest.TestCase):

    def test_validSearch(self):
        baseURL = "http://www.amazon.com"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.implicitly_wait(3)
        driver.get(baseURL)


        hp = HomePage(driver)
        hp.searchFor("Echo Show")




        driver.close()
