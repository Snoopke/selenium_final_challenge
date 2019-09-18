from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_product_to_basket(self):
        button = self.browser.find_element(*ProductPageLocators.BASKET)
        assert self.is_element_present(*ProductPageLocators.BASKET), "Add to basket button is not presented"
        button.click()
