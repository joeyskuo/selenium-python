from pages.home_page import HomePage
from pages.product_page import ProductPage
import pytest

@pytest.mark.usefixtures("setUp")
class Test_BannerToCart():

    @pytest.fixture(autouse=True)
    def classSetup(self, setUp):
        self.hp = HomePage(self.driver)
        self.pp = ProductPage(self.driver)

    def test_addToCart(self):
        self.hp.clickInlineBanner()
        self.pp.clickAddToCartButton()
        result = self.pp.verifyAddToCartSuccessful()
        assert result == True