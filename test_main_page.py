import pytest
from .pages.basket_page import BasketPage

from .pages.main_page import MainPage
link = "http://selenium1py.pythonanywhere.com/"

@pytest.mark.login_guest()
class TestLoginFromMainPage():
    def test_guest_can_go_to_login_page(self, browser):
        page = MainPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        page.open()  # открываем страницу
        page.go_to_login_page()  # выполняем метод страницы - переходим на страницу логина

    def test_guest_should_see_login_link(self, browser):
        page = MainPage(browser, link)
        page.open()
        page.should_be_login_link()

    def test_guest_cant_see_product_in_basket_opened_from_main_page(self, browser):
        page = MainPage(browser, link)
        page.open()
        page.go_to_basket_page()
        page = BasketPage(browser, link)
        page.should_not_be_products_in_basket()
        page.should_be_empty_basket_message()