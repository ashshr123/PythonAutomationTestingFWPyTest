from Config.TestData import TestData
from Pages.BasePage import BasePage
from selenium.webdriver.common.by import By

from Pages.SearchPage import SearchPage


class HomePage(BasePage):

    SEARCHBOX=(By.XPATH,"//*[@id='twotabsearchtextbox']")
    SEARCHBUTTON=(By.XPATH,"//input[@type='submit' and @value]")


    def __init__(self,driver):
          super().__init__(driver)
          self.driver.get(TestData.BASE_URL)

    def click_search_home(self):
          self.do_click(self.SEARCHBOX)

    def send_keys_home(self):
          self.do_send_keys(self.SEARCHBOX,"Apple Ipad Mini")
    def click_searchbtn_home(self):
          self.do_click(self.SEARCHBUTTON)
          return SearchPage(self.driver)

    def verify_title_home(self):
        return self.get_title(TestData.TITLE)
