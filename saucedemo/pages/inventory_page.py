from saucedemo.pages.base_page import BasePage
from saucedemo.locators.locators_inventory_page import LocatorsInventoryPage
from saucedemo.test_data.data_inventory_page import DataInventoryPage

locator = LocatorsInventoryPage
data = DataInventoryPage


class InventoryPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    # def add_in_busket(self):