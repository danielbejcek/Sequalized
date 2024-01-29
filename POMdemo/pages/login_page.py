from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

class CookieClicker:
    def __init__(self, driver):
        """Defining locators"""
        self.driver = driver
        self.language_element = (By.ID,"langSelect-EN")

        self.cookie_element = (By.ID,"bigCookie")
        self.cookie_counter_element = (By.ID,"cookies")
        self.cursor_price = (By.ID, "productPrice0")
        self.grandma_price = (By.ID, "productPrice1")
        self.purchase_list = []
        self.actions = ActionChains(driver)

    def open_page(self,url):
        self.driver.get(url)
    def cookie_manager(self):
        try:
            cookies_1 = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, "fc-footer-buttons")))
            accept_all_1 = cookies_1.find_element(By.CLASS_NAME, "fc-primary-button").click()
        finally:
            time.sleep(2)

    def select_language(self):
        self.driver.implicitly_wait(3)
        self.driver.find_element(*self.language_element).click()

    def close_cookies(self):
        try:
            self.driver.implicitly_wait(3)
            cookies_2 = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, "cc_container--open")))
            accept_all_2 = cookies_2.find_element(By.LINK_TEXT, "Got it!").click()
            self.driver.implicitly_wait(3)
            cookies_3 = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, "google-revocation-link-placeholder")))
            accept_all_3 = cookies_3.find_element(By.CSS_SELECTOR, "[aria-label='Close']").click()
        finally:
            time.sleep(2)
    def back_up_icon(self):
        self.driver.implicitly_wait(1)
        save_icon = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.ID, "notes")))
        close_icon = save_icon.find_element(By.CLASS_NAME, "close").click()


    def action_chain_cookie_click(self):
        for i in range(100):
            self.actions.double_click(self.driver.find_element(*self.cookie_element))
            self.actions.perform()
            """Locating the text property of the HTML element 'cookies' and striping it of the rest of the text"""
            count = int(self.driver.find_element(*self.cookie_counter_element).text.split(" ")[0])
            print(count)
            cookie_cursor = int(self.driver.find_element(*self.cursor_price).text)
            if count >= cookie_cursor:
                self.actions.move_to_element(self.driver.find_element(*self.cursor_price))
                self.actions.click()
                self.actions.perform()










