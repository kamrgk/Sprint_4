from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators.order_scooter_page_locators import OrderScooterLocators as Locators
import allure


class OrderScooter:
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Ждем пока Заказать станет кликабельна')
    def wait_order_button_in_header_to_be_clickable(self):
        WebDriverWait(self.driver, 5).until(
            expected_conditions.element_to_be_clickable(Locators.order_button_in_header)
        )

    @allure.step('Тап по кнопке Заказать в хэдере')
    def click_to_order_button_in_header(self, order_button_locator):
        self.driver.find_element(*order_button_locator).click()

    @allure.step('Проверяем что открыта страница заказа')
    def check_is_order_page_opened(self):
        assert self.driver.current_url == "https://qa-scooter.praktikum-services.ru/order"

    def open_order_page_from_header_button(self):
        self.wait_order_button_in_header_to_be_clickable()
        self.click_to_order_button_in_header(Locators.order_button_in_header)
        self.check_is_order_page_opened()

    @allure.step('Скролл к кнопке Заказать в бади')
    def scroll_to_order_button_in_body(self):
        order_button_in_body_element = self.driver.find_element(*Locators.order_button_in_body)
        self.driver.execute_script("arguments[0].scrollIntoView();", order_button_in_body_element)

    @allure.step('Ждем что кнопка Заказать в бади кликабельна')
    def wait_order_button_in_body_to_be_clickable(self):
        WebDriverWait(self.driver, 5).until(
            expected_conditions.element_to_be_clickable(Locators.order_button_in_body)
        )

    def open_order_page_from_body_button(self):
        self.scroll_to_order_button_in_body()
        self.wait_order_button_in_body_to_be_clickable()
        self.click_to_order_button_in_header(Locators.order_button_in_body)
        self.check_is_order_page_opened()

    @allure.step('Заполняем текстое поле {input_field} значением {value}')
    def send_keys_to_order_scooter(self, input_field, value):
        self.driver.find_element(*input_field).send_keys(value)

    @allure.step('Выбираем станцию метро')
    def choose_metro(self):
        self.driver.find_element(*Locators.metro).click()
        WebDriverWait(self.driver, 5).until(
            expected_conditions.visibility_of_element_located(Locators.metro_selection)
        )
        self.driver.find_element(*Locators.metro_test_value).click()

    @allure.step('Заполняем информацию о заказчике')
    def fill_info_about_client(self, name, surname, address, phone):
        self.send_keys_to_order_scooter(Locators.name, name)
        self.send_keys_to_order_scooter(Locators.surname, surname)
        self.send_keys_to_order_scooter(Locators.address, address)
        self.send_keys_to_order_scooter(Locators.phone, phone)

        self.choose_metro()

    @allure.step('Тапаем по кнопке Далее и ждем что открылся второй этап оформления заказа')
    @allure.description('Определяем что второй этап открылся через видимость кнопка Назад')
    def open_next_step_of_order(self):
        self.driver.find_element(*Locators.next).click()
        WebDriverWait(self.driver, 5).until(
            expected_conditions.element_to_be_clickable(Locators.back)
        )

    @allure.step('Выбираем дату заказа')
    def choose_date(self):
        self.driver.find_element(*Locators.date).click()
        WebDriverWait(self.driver, 5).until(
            expected_conditions.element_to_be_clickable(Locators.date_picker)
        )
        self.driver.find_element(*Locators.date_test_value).click()

    @allure.step('Выбираем период аренды')
    def choose_rental_period(self):
        self.driver.find_element(*Locators.rental_period).click()
        WebDriverWait(self.driver, 5).until(
            expected_conditions.element_to_be_clickable(Locators.rental_period_dropdown)
        )
        self.driver.find_element(*Locators.rental_period_test_value).click()

    @allure.step('Выбираем цвет самоката')
    def choose_scooter_color(self):
        self.driver.find_element(*Locators.scooter_color).click()
        WebDriverWait(self.driver, 5).until(
            expected_conditions.element_to_be_clickable(Locators.scooter_color_selected)
        )

    @allure.step('Оставляем комментарий, если он не пустой: {comment}')
    def set_comment(self, comment):
        self.driver.find_element(*Locators.comment).send_keys(comment)

    @allure.step('Ждем на кнопку заказать и ждем форму подтверждения заказа')
    def click_order_to_filled_order(self):
        self.driver.find_element(*Locators.order_button_in_body).click()
        WebDriverWait(self.driver, 5).until(
            expected_conditions.visibility_of_element_located(Locators.approve_order_modal)
        )

    @allure.step('Подтверждаем заказ и жмем на кнопку Посмотреть статус')
    def approve_order_and_check_status(self):
        self.driver.find_element(*Locators.yes_button).click()
        WebDriverWait(self.driver, 5).until(
            expected_conditions.visibility_of_element_located(Locators.order_successful)
        )
        self.driver.find_element(*Locators.check_status).click()

    @allure.step('Второй этап заполнения информации о заказе')
    def fill_info_about_order_all_fields(self, comment=""):
        # дата аренды
        self.choose_date()

        # срок аренды
        self.choose_rental_period()

        # цвет самоката
        self.choose_scooter_color()

        # комментарий для курьера
        self.set_comment(comment=comment)

        self.click_order_to_filled_order()
        self.approve_order_and_check_status()

    @allure.step('Ждем чтобы логотип Самокат был кликабелен и тапаем на него и проверяем, что открылась главная страница Самокат')
    def click_to_scooter_logo_in_header(self):
        WebDriverWait(self.driver, 5).until(
            expected_conditions.element_to_be_clickable(Locators.scooter_header_logo)
        )
        self.driver.find_element(*Locators.scooter_header_logo).click()

        WebDriverWait(self.driver, 5).until(
            expected_conditions.element_to_be_clickable(Locators.study_logo)
        )

        assert self.driver.current_url == "https://qa-scooter.praktikum-services.ru/"

    @allure.step('Ждем чтобы логотип Яндекс был кликабелен и тапаем на него и проверяем, что открылась главная страница Яндекс')
    def click_to_yandex_logo_in_header(self):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable(Locators.yandex_header_logo)
        )
        self.driver.find_element(*Locators.yandex_header_logo).click()

        WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable(Locators.yandex_search)
        )

        assert self.driver.current_url == "https://dzen.ru/?yredirect=true"
