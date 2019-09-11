from .base_page import BasePage
'''импортируем класс из base_page, чтобы main page унаследовал атрибуты'''
from selenium.webdriver.common.by import By

class MainPage(BasePage):
    def go_to_login_page(self):
        login_link = self.browser.find_element(By.CSS_SELECTOR, "#login_link")
        login_link.click()
