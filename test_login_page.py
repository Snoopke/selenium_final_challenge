from .pages.login_page import LoginPage
link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"

def test_should_be_login_url(browser):
    page = LoginPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()  # открываем страницу
    page.should_be_login_url()  # выполняем метод страницы - переходим на страницу логина

def test_should_be_login_form(browser):
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_form()