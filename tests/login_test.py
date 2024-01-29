import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import pytest
from POMdemo.pages.login_page import CookieClicker



@pytest.fixture()
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    yield driver

# @pytest.mark.parametrize("username, password",[
#     ("test","test"),
#     ("user2","pass2"),
#     ("user3","pass3")])


def test_website_2(driver):
    webpage = CookieClicker(driver)
    webpage.open_page("https://orteil.dashnet.org/cookieclicker/")

    webpage.cookie_manager()
    webpage.select_language()
    time.sleep(2)
    webpage.close_cookies()
    time.sleep(1)
    webpage.back_up_icon()
    time.sleep(2)
    webpage.action_chain_cookie_click()


