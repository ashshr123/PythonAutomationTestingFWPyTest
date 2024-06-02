# Python Automation Testing Framework with Selenium and PyTest

This repository contains an automation testing framework for testing the Amazon.in website using Selenium and PyTest in Python. The framework follows the Page Object Model (POM) design pattern for better test maintenance and readability.




### Directory and File Descriptions

#### `Config/`

Contains final key words , values and URL's

#### `Pages/`

Contains the Page Object Model (POM) classes for the web pages under test.

#### `Tests/`
Contains the test cases.

#### `conftest.py`

'''python
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
    web_driver.quit()'''



