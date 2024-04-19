from saucedemo.pages.start_page import StartPage
from saucedemo.test_data.data_start_page import DataStartPage


class TestLogin:
    data = DataStartPage

    def test_auth_positive(self, driver):
        start_page = StartPage(driver)

        start_page.login()

        assert driver.current_url == self.data.url_inventory_page, 'Неверный адрес'


    def test_auth_negative(self, driver):
        start_page = StartPage(driver)

        start_page.login(self.data.er_name, self.data.er_pass)

        assert start_page.text_error_auth(driver) == self.data.error_auth, 'Некорректное сообщение при ошибке авторизации'