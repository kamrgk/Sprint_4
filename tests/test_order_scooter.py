from selenium import webdriver
import allure
from pages.order_scooter_page import OrderScooter


class TestOrderScooter:
    driver = None

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.maximize_window()

    @allure.step('Заполняем форму заказа самоката')
    @allure.title('Заказываем самокат с заполнением в том числе необязательных полей')
    @allure.description('Заказываем самокат и видим модельное окно успешного результата заказа')
    def test_order_scooter_with_unnecessary_order_fields_from_header_button(self):
        name = "Камилла"
        surname = "Демьяненко"
        address = "Ленина 1"
        phone = "+77777777777"

        self.driver.get("https://qa-scooter.praktikum-services.ru/")
        order_scooter = OrderScooter(self.driver)
        order_scooter.open_order_page_from_header_button()
        order_scooter.fill_info_about_client(name, surname, address, phone)
        order_scooter.open_next_step_of_order()

        order_scooter.fill_info_about_order_all_fields(comment="Тестовый комментарий")

    @allure.step('Заполняем форму заказа самоката')
    @allure.title('Заказываем самокат с заполнением без необязательных полей')
    @allure.description('Заказываем самокат и видим модельное окно успешного результата заказа')
    def test_order_scooter_without_unnecessary_order_fields_from_header_button(self):
        name = "Тестовый"
        surname = "Пользователь"
        address = "Тестовый адрес 1"
        phone = "+71234567890"

        self.driver.get("https://qa-scooter.praktikum-services.ru/")
        order_scooter = OrderScooter(self.driver)
        order_scooter.open_order_page_from_body_button()
        order_scooter.fill_info_about_client(name, surname, address, phone)
        order_scooter.open_next_step_of_order()

        order_scooter.fill_info_about_order_all_fields()

    @allure.step('Проверяем переход на главную сайта через лого')
    @allure.title('Тап на лого Самокат')
    @allure.description('Тапаем и ждем, пока откроется главная страница сайта')
    def test_open_main_page_by_click_logo_in_header(self):
        order_scooter = OrderScooter(self.driver)
        order_scooter.click_to_scooter_logo_in_header()

    @allure.step('Проверяем переход на сайт Яндекс через лого')
    @allure.title('Тап на лого Яндекс')
    @allure.description('Тапаем и ждем, пока откроется сайт Яндекс')
    def test_open_yandex_page_by_click_logo_in_header(self):
        order_scooter = OrderScooter(self.driver)
        order_scooter.click_to_yandex_logo_in_header()

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
