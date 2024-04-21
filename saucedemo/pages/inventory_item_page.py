from saucedemo.pages.base_page import BasePage
from saucedemo.locators.locators_inventory_item_page import LocatorsInventoryItemPage
# from saucedemo.test_data.data_inventory_page import DataInventoryPage

# locator = LocatorsInventoryItemPage
# data = DataInventoryItemPage


class InventoryItemPage(BasePage):
    locator = LocatorsInventoryItemPage

    def __init__(self, driver):
        super().__init__(driver)

    def add_in_busket(self, locator):
        self.driver.find_element(*locator).click()
        self.driver.find_element(*self.locator.add_to_cart).click()




