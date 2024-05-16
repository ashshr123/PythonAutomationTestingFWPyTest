from Config.TestData import TestData
from Pages.HomePage import HomePage
from Pages.SearchPage import SearchPage
from Tests.test_Base import Test_Base
from Tests.test_homepage import Test_Home


class Test_Search(Test_Base):

    def test_verify_search(self):
        self.homepage = HomePage(self.driver)
        self.homepage.click_search_home()
        self.homepage.send_keys_home()
        searchpage=self.homepage.click_searchbtn_home()
        try:
            assert TestData.TEXT == searchpage.get_text_search()
        except Exception:
            self.driver.save_screenshot("snap.png")
            raise Exception("Assert failed")