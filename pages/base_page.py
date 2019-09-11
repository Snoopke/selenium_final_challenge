from selenium.common.exceptions import NoSuchElementException

class BasePage():
    def __init__(self, browser, url):
        """Конструктор класса етод, который вызывается, когда мы создаем объект.
         Конструктор объявляется ключевым словом __init__.
        В него в качестве параметров мы передаем экземпляр драйвера и url адрес."""
        self.browser = browser
        self.url = url

    def open(self):
        """метод открывает нужную страницу, используя метод get() """
        self.browser.get(self.url)

    def is_element_present(self, how, what):
        '''Метод ищет элемент на странице'''
        try:
            self.browser.find_element(how, what)
        except (NoSuchElementException):
            return False
        return True