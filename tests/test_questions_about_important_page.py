from selenium import webdriver
from pages.questions_about_important_page import QuestionsAboutImportant
import allure


class TestQuestionsAboutImportant:
    driver = None

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.maximize_window()
        cls.driver.get("https://qa-scooter.praktikum-services.ru/")

    @allure.step('Тапаем на вопрос и проверяем ответ')
    @allure.title('Сколько это стоит? И как оплатить?')
    @allure.description('Ожидаем, что раскроется div и отобразится ответ')
    def test_click_to_what_is_the_price(self):
        questions_about_important = QuestionsAboutImportant(self.driver)
        questions_about_important.scroll_questions_about_important_block()
        questions_about_important.click_to_what_is_the_prise()
        questions_about_important.check_what_is_the_prise_answer_visible()

    @allure.step('Тапаем на вопрос и проверяем ответ')
    @allure.title('Хочу сразу несколько самокатов! Так можно?')
    @allure.description('Ожидаем, что раскроется div и отобразится ответ')
    def test_click_to_several_scooters(self):
        questions_about_important = QuestionsAboutImportant(self.driver)
        questions_about_important.scroll_questions_about_important_block()
        questions_about_important.click_to_several_scooters()
        questions_about_important.check_several_scooters_visible()

    @allure.step('Тапаем на вопрос и проверяем ответ')
    @allure.title('Как рассчитывается время аренды?')
    @allure.description('Ожидаем, что раскроется div и отобразится ответ')
    def test_click_to_time_of_rent(self):
        questions_about_important = QuestionsAboutImportant(self.driver)
        questions_about_important.scroll_questions_about_important_block()
        questions_about_important.click_to_time_of_rent()
        questions_about_important.check_time_of_rent_visible()

    @allure.step('Тапаем на вопрос и проверяем ответ')
    @allure.title('Можно ли заказать самокат прямо на сегодня')
    @allure.description('Ожидаем, что раскроется div и отобразится ответ')
    def test_click_to_order_today(self):
        questions_about_important = QuestionsAboutImportant(self.driver)
        questions_about_important.scroll_questions_about_important_block()
        questions_about_important.click_to_order_today()
        questions_about_important.check_order_today_visible()

    @allure.step('Тапаем на вопрос и проверяем ответ')
    @allure.title('Можно ли продлить заказ или вернуть самокат раньше?')
    @allure.description('Ожидаем, что раскроется div и отобразится ответ')
    def test_click_to_extend_or_return_order(self):
        questions_about_important = QuestionsAboutImportant(self.driver)
        questions_about_important.scroll_questions_about_important_block()
        questions_about_important.click_to_extend_or_return_order()
        questions_about_important.check_extend_or_return_order_visible()

    @allure.step('Тапаем на вопрос и проверяем ответ')
    @allure.title('Вы привозите зарядку вместе с самокатом?')
    @allure.description('Ожидаем, что раскроется div и отобразится ответ')
    def test_click_to_charger(self):
        questions_about_important = QuestionsAboutImportant(self.driver)
        questions_about_important.scroll_questions_about_important_block()
        questions_about_important.click_to_charger()
        questions_about_important.check_charger_visible()

    @allure.step('Тапаем на вопрос и проверяем ответ')
    @allure.title('Можно ли отменить заказ?')
    @allure.description('Ожидаем, что раскроется div и отобразится ответ')
    def test_click_cancel_order(self):
        questions_about_important = QuestionsAboutImportant(self.driver)
        questions_about_important.scroll_questions_about_important_block()
        questions_about_important.click_to_cancel_order()
        questions_about_important.check_cancel_order_visible()

    @allure.step('Тапаем на вопрос и проверяем ответ')
    @allure.title('Я жизу за МКАДом, привезёте?')
    @allure.description('Ожидаем, что раскроется div и отобразится ответ')
    def test_click_outside_mkad(self):
        questions_about_important = QuestionsAboutImportant(self.driver)
        questions_about_important.scroll_questions_about_important_block()
        questions_about_important.click_to_outside_mkad()
        questions_about_important.check_outside_mkad_visible()

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
