from pages.home_page import HomePage
import pytest

@pytest.mark.usefixtures("setUp")
class Test_SearchFeature():

    @pytest.fixture(autouse=True)
    def classSetup(self, setUp):
        self.hp = HomePage(self.driver)

    def test_validSearch(self):
        self.hp.searchFor("Echo Show")
        result = self.hp.verifySearchResult("Echo Show")
        assert result == True




