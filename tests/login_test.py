import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import pytest
from POMdemo.pages.login_page import LoginPage




@pytest.fixture()
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.get("https://trytestingthis.netlify.app/")

    """Surpass Google cookies window"""
    # cookies_popup = WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.ID, "CXQnmb")))
    # accept_all_button = cookies_popup.find_element(By.ID, "L2AGLb").click()

    yield driver
    driver.close()
    driver.quit()

# @pytest.mark.parametrize("username, password",[
#     ("test","test"),
#     ("user2","pass2"),
#     ("user3","pass3")])

def test_login(driver):
    login_page = LoginPage(driver)
    login_page.open_page("https://trytestingthis.netlify.app/")
    time.sleep(2)
    login_page.enter_username("test")
    login_page.enter_password("test")
    time.sleep(2)
    login_page.submit_login()


