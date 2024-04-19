from saucedemo.pages.start_page import StartPage
from saucedemo.test_data.data_start_page import DataStartPage

data = DataStartPage


class TestLogin:

    def test_auth_positive(self, driver):
        start_page = StartPage(driver)

        start_page.login()

        assert driver.current_url == data.url_inventory_page, 'Неверный адрес'


    def test_auth_negative(self, driver):
        start_page = StartPage(driver)

        start_page.login(data.er_name, data.er_pass)

        assert start_page.text_error_auth() == data.error_auth, 'Некорректное сообщение при ошибке авторизации'