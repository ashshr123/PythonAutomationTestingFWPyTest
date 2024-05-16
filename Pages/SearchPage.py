from Config.TestData import TestData
from Pages.BasePage import BasePage
from selenium.webdriver.common.by import By

class SearchPage(BasePage):

      RESULT = (By.XPATH, "//span[text()='Apple iPad Mini (6th Generation): with A15 Bionic chip, 21.08 cm (8.3″) Liquid Retina Display, 64GB, Wi-Fi 6, 12MP front/12MP Back Camera, Touch ID, All-Day Battery Life – Space Grey']")

      def __init__(self, driver):
          super().__init__(driver)

      def get_text_search(self):
          return self.get_text(self.RESULT)
