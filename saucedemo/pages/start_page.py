from saucedemo.pages.base_page import BasePage
from saucedemo.locators.locators_start_page import LocatorsStartPage
from saucedemo.test_data.data_start_page import DataStartPage


class StartPage(BasePage):
    locator = LocatorsStartPage
    data = DataStartPage

    def __init__(self, driver):
        super().__init__(driver)

    def text_error_auth(self):
        return self.get_txt(self.locator.error_auth)