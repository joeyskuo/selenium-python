
from selenium import webdriver
import pytest

@pytest.yield_fixture(scope="class")
def setUp(request):
    baseURL = "http://www.amazon.com"
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.implicitly_wait(3)
    driver.get(baseURL)

    if request.cls is not None:
        request.cls.driver = driver

    yield driver

    driver.close()