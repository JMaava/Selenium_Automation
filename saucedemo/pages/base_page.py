from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as wait
from saucedemo.locators.locators_start_page import LocatorsStartPage
from saucedemo.test_data.data_start_page import DataStartPage
from saucedemo.locators.locators_cart_page import LocatorsCartPage


class BasePage:
    locator = LocatorsStartPage()
    data = DataStartPage()
    locator_cart_page = LocatorsCartPage()

    timeout = 10

    def __init__(self, driver):
        self.driver = driver
        # self.find_element = driver.find_element

    def send_keys(self, locator:tuple, text:str):
        self.driver.find_element(*locator).send_keys(text)

    def click(self, locator:tuple):
        self.driver.find_element(*locator).click()

    def open(self):
        self.driver.get(self.data.url)

    def login(self, name=data.name, password=data.password):
        self.send_keys(self.locator.input_user_name, name)
        self.send_keys(self.locator.input_password, password)
        self.click(self.locator.button_login)

    def get_txt(self, locator):
        txt = self.driver.find_element(*locator).text
        return txt

    def clean_basket(self):
        self.click(self.locator_cart_page.btn_remove)

    def element_is_clickable(self, locator, timeout=timeout):
        return wait(self.driver, timeout).until(EC.element_to_be_clickable(locator))

    def element_is_visible(self, locator, timeout=timeout):
        return wait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    def elements_are_visible(self, locator, timeout=timeout):
        return wait(self.driver, timeout).until(EC.visibility_of_all_elements_located(locator))




