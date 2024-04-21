from saucedemo.pages.base_page import BasePage
from saucedemo.locators.locators_cart_page import LocatorsCartPage



class CartPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

