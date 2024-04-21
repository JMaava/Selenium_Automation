import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from saucedemo.test_data.data_start_page import DataStartPage
from saucedemo.pages.start_page import StartPage

data = DataStartPage
url = "https://www.saucedemo.com/"

@pytest.fixture
def driver():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--window-size=1920,1080")
    service = Service(executable_path=ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    # driver.implicitly_wait(10)
    driver.get(url)
    #     start_page = StartPage(driver)
    #     start_page.open()
    yield driver
    print('\nquit browser...')
    driver.quit()
