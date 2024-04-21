from selenium.webdriver.common.by import By


class LocatorsInventoryPage:

    name_page = (By.XPATH, '//span[@data-test="title"]')
    item_name = (By.XPATH, '//*[@data-test="inventory-item-name"]')