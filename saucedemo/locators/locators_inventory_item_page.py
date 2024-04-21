from selenium.webdriver.common.by import By


class LocatorsInventoryItemPage:

    add_to_cart = (By.XPATH, '//*[@data-test="add-to-cart"]')
    item_name = (By.XPATH, '//a[@data-test="item-4-title-link"]')
    lst_item_name = [(By.XPATH, '//a[@data-test="item-4-title-link"]'),
                 (By.XPATH, '//a[@data-test="item-0-title-link"]'),
                 (By.XPATH, '//a[@data-test="item-1-title-link"]'),
                 (By.XPATH, '//a[@data-test="item-5-title-link"]'),
                 (By.XPATH, '//a[@data-test="item-2-title-link"]'),
                 (By.XPATH, '//a[@data-test="item-3-title-link"]')]
