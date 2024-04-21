import pytest
from saucedemo.pages.base_page import BasePage
from saucedemo.pages.inventory_item_page import InventoryItemPage
from saucedemo.locators.locators_inventory_item_page import LocatorsInventoryItemPage
from saucedemo.locators.locator_header import LocatorsHeader
from saucedemo.locators.locators_cart_page import LocatorsCartPage
from saucedemo.test_data.data_start_page import DataStartPage
from saucedemo.pages.cart_page import CartPage


class TestProductCard:

    locator_item = LocatorsInventoryItemPage()
    locator_header = LocatorsHeader()
    locator_cart = LocatorsCartPage()

    @pytest.mark.parametrize("lst_item_name", locator_item.lst_item_name)
    def test_add_product_card(self, driver, lst_item_name):

        base_page = BasePage(driver)
        base_page.login()

        inventory_item_page = InventoryItemPage(driver)
        item_list = inventory_item_page.get_txt(lst_item_name)
        inventory_item_page.add_in_basket(lst_item_name)

        inventory_item_page.click(self.locator_header.cart_link)
        item_in_basket = inventory_item_page.get_txt(self.locator_cart.item_name)

        base_page.clean_basket()
        assert item_in_basket == item_list


