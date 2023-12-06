import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromseService
from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome(service=ChromseService(ChromeDriverManager().install()))
driver.get("https://www.google.com")

"""Surpass cookies window"""
cookies_popup = WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.ID, "CXQnmb")))
accept_all_button = cookies_popup.find_element(By.ID, "L2AGLb").click()

"""Google search bar input"""
search = driver.find_element(By.ID,"APjFqb")
search.send_keys("Automation")
search.send_keys(Keys.RETURN)

time.sleep(2)
driver.quit()


