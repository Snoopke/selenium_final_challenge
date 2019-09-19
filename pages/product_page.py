from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_product_to_basket(self):
        button = self.browser.find_element(*ProductPageLocators.BASKET)
        assert self.is_element_present(*ProductPageLocators.BASKET), "Add to basket button is not presented"
        button.click()

    def notification_about_adding(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        message = self.browser.find_element(*ProductPageLocators.MESSAGE_ABOUT_ADDING).text
        assert product_name == message, "Added another product"

    def check_total_price(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        total_price = self.browser.find_element(*ProductPageLocators.PRICE_BASKET_TOTAL).text
        assert product_price == total_price, 'Wrong total price'

