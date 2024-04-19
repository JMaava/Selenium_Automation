from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait as wait
from saucedemo.locators.locators_start_page import LocatorsStartPage
from saucedemo.test_data.data_start_page import DataStartPage
from saucedemo.locators.locators_cart_page import LocatorsCartPage

locator = LocatorsStartPage
data = DataStartPage
locator_cart_page = LocatorsCartPage

class BasePage:

    timeout = 10

    def __init__(self, driver):
        self.driver = driver
        self.find_element = driver.find_element

    def find(self, args):
        self.driver.find_element(*args)

    def send_keys(self, locator:tuple, text:str):
        self.driver.find_element(*locator).send_keys(text)

    def click(self, driver, locator:tuple):
        driver.find_element(*locator).click()

    def open(self):
        self.driver.get(data.url)

    def input_user_name_send_keys(self, text):
        self.send_keys(locator.input_user_name, text)

    def input_password_send_keys(self, text):
        self.send_keys(locator.input_password, text)

    def click_button_login(self):
        self.click(self, locator.button_login)

    def login(self, name=data.name, password=data.password):

        self.input_user_name_send_keys(name)
        self.input_password_send_keys(password)
        self.click_button_login()

    def get_txt(self, driver, locator):
        txt = driver.find_element(*locator).text
        return txt

    def clean_basket(self, driver):
        self.click(driver, locator_cart_page.btn_remove)

    def element_is_clickable(self, locator, timeout=timeout):
        return wait(self.driver, timeout).until(EC.element_to_be_clickable(locator))

    def element_is_visible(self, locator, timeout=timeout):
        return wait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    def elements_are_visible(self, locator, timeout=timeout):
        return wait(self.driver, timeout).until(EC.visibility_of_all_elements_located(locator))




