import pytest
from selenium import webdriver

from Config.TestData import TestData


@pytest.fixture(params=[TestData.BROWSER], scope='class')
def init_driver(request):
    if request.param == "chrome":
        chrome_options = webdriver.ChromeOptions()
        driver_path = TestData.DRIVER_PATH
        web_driver = webdriver.Chrome(options=chrome_options)
    if request.param == "safari":
        web_driver = webdriver.Safari()
    request.cls.driver = web_driver
    yield
    web_driver.quit()