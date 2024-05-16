from Pages.HomePage import HomePage
from Tests.test_Base import Test_Base


class Test_Home(Test_Base):

    def test_enterandsearch(self):
        self.homepage = HomePage(self.driver)
        self.homepage.click_search_home()
        self.homepage.send_keys_home()
        self.homepage.click_searchbtn_home()
        self.driver.save_screenshot("screenshot.png")



