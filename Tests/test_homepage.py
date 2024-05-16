from Config.TestData import TestData
from Pages.HomePage import HomePage
from Tests.test_Base import Test_Base


class Test_Home(Test_Base):

    def test_title(self):
        self.homepage = HomePage(self.driver)
        title = self.homepage.verify_title_home()
        try:
            assert TestData.TITLE == title
        except Exception:
            self.driver.save_screenshot("screenshot1.png")
            raise Exception("Assert Failed")

    def test_enterandsearch(self):
        self.homepage = HomePage(self.driver)
        self.homepage.click_search_home()
        self.homepage.send_keys_home()
        self.homepage.click_searchbtn_home()
        try:
            assert True
        except Exception as e:
            print(e)
            self.driver.save_screenshot("screenshot.png")
            raise Exception("Assert failed")
