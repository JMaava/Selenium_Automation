from saucedemo.pages.base_page import BasePage
from saucedemo.locators.locators_cart_page import LocatorsCartPage



class CartPage(BasePage):

    # locator_cart_page = LocatorsCartPage

    def __init__(self, driver):
        super().__init__(driver)

    # def clean_busket(self, driver):
    #     self.click(self, driver, self.locator_cart_page.btn_remove)
