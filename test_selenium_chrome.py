import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import pytest




@pytest.fixture()
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    # driver.get("https://www.google.com")
    driver.get("https://trytestingthis.netlify.app/")

    """Surpass cookies window"""
    # cookies_popup = WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.ID, "CXQnmb")))
    # accept_all_button = cookies_popup.find_element(By.ID, "L2AGLb").click()
    yield driver
    driver.close()
    driver.quit()

#
# def test_google_search(driver):
#     """Google search bar input"""
#     search = driver.find_element(By.ID,"APjFqb")
#     search.send_keys("Selenium Python")
#     search.send_keys(Keys.RETURN)
#     time.sleep(2)
@pytest.mark.parametrize("username, password",[
    ("test","test"),
    ("user2","pass2"),
    ("user3","pass3")])

def test_login_input(driver, username, password):
    user_name_loc = driver.find_element(By.ID, "uname")
    pwd_loc = driver.find_element(By.ID, "pwd")

    user_name_loc.send_keys(username)
    pwd_loc.send_keys(password)
    login_btn = driver.find_element(By.XPATH,"//input[@value='Login']").click()
    assert "Successful" in driver.page_source


