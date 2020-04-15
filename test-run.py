from selenium.webdriver.common.keys import Keys
import pytest


@pytest.fixture
def chrome_options(chrome_options, pytestconfig):
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('--no-sandbox')
    return chrome_options


def test_page_title(selenium):
    selenium.implicitly_wait(15)
    selenium.maximize_window()
    selenium.get('https://2ip.ru')
    assert 'VPN' in selenium.page_source


def test_wrong_page_title(selenium):
    selenium.implicitly_wait(15)
    selenium.maximize_window()
    selenium.get('https://2ip.ru')
    assert 'VPN' in selenium.page_source
