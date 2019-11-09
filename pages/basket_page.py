from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_empty_basket_message(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET_MESSAGE), \
            'No empty basket message, but it should'

    def should_be_product_in_basket(self):
        assert self.is_element_present(*BasketPageLocators.PRODUCT_IN_BASKET), \
            'No products in basket'

    def should_not_be_products_in_basket(self):
        assert not self.is_element_present(*BasketPageLocators.PRODUCT_IN_BASKET), \
            "Products in basket, but shouldn't"
