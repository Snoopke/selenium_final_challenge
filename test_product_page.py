from .pages.product_page import ProductPage
from selenium.common.exceptions import NoAlertPresentException

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"

def test_guest_can_add_product_to_basket(browser):
    page = ProductPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()  # открываем страницу
    page.add_product_to_basket()  # выполняем метод страницы - добавляем в корзину
    page.solve_quiz_and_get_code()
