from selenium.webdriver.common.by import By


class LocatorsStartPage:

    input_user_name = (By.XPATH, '//input[@id="user-name"]')
    input_password = (By.XPATH, '//input[@id="password"]')
    button_login = (By.CSS_SELECTOR, '#login-button')
    error_auth = (By.XPATH, '//*[@data-test="error"]')
