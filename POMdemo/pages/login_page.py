from selenium.webdriver.common.by import By

class LoginPage:
    def __init__(self, driver):
        """Defining locators"""
        self.driver = driver
        self.username_textbox = (By.ID, "uname")
        self.password = (By.ID, "pwd")
        self.login_button = (By.XPATH,"//input[@value='Login']")

    def open_page(self, url):
        self.driver.get(url)

    def enter_username(self, username):
        self.driver.find_element(*self.username_textbox).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(*self.password).send_keys(password)

    def submit_login(self):
        self.driver.find_element(*self.login_button).click()


