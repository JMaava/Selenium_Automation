from selenium.webdriver.common.by import By


class LocatorsCartPage:

    item_name = (By.XPATH, '//div[@data-test="inventory-item-name"]')
    btn_remove = (By.XPATH, '//button[contains(@class, "cart_button")]')