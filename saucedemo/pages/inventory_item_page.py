from saucedemo.pages.base_page import BasePage
from saucedemo.locators.locators_inventory_item_page import LocatorsInventoryItemPage


class InventoryItemPage(BasePage):
    locator = LocatorsInventoryItemPage()

    def __init__(self, driver):
        super().__init__(driver)

    def add_in_basket(self, locator):
        self.driver.find_element(*locator).click()
        self.driver.find_element(*self.locator.add_to_cart).click()




