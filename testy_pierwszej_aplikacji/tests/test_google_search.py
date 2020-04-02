from selenium import webdriver
from page_object_patern.google_home_page import GoogleHomePage
from page_object_patern.google_result_page import GoogleResultPage

import pytest
from webdriver_manager.firefox import GeckoDriverManager


class TestGoogleSearch:

    @pytest.fixture ()
    def setup(self):
        self.driver = webdriver.Firefox (executable_path=GeckoDriverManager ().install ())
        self.driver.implicitly_wait (10)
        self.driver.maximize_window ()
        # # yield
        # self.driver.quit ()

    def test_google_search(self, setup):
        self.driver.get ("http://google.com")
        home_page = GoogleHomePage(self.driver)
        home_page.search_in_google('Selenium')
        result_page = GoogleResultPage(self.driver)
        result_page.open_first_result()




