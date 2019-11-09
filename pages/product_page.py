from .base_page import BasePage
from .locators import ProductPageLocators
from .locators import BasketPageLocators


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

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_be_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), "Success message don't disappeared"

    def should_be_empty_basket_message(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET_MESSAGE), \
            'No empty basket message, but it should'

    def should_be_product_in_basket(self):
        assert self.is_element_present(*BasketPageLocators.PRODUCT_IN_BASKET), \
            'No products in basket'

    def should_not_be_products_in_basket(self):
        assert not self.is_element_present(*BasketPageLocators.PRODUCT_IN_BASKET), \
            "Products in basket, but shouldn't"