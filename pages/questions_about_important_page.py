from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators.questions_about_important_page_locators import QuestionsAboutImportantLocators as Locators
import allure


class QuestionsAboutImportant:
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Скролл до блока с вопросами')
    def scroll_questions_about_important_block(self):
        questions_about_important_element = self.driver.find_element(*Locators.questions_about_important_block)
        self.driver.execute_script("arguments[0].scrollIntoView();", questions_about_important_element)
        WebDriverWait(self.driver, 5).until(
            expected_conditions.visibility_of_element_located(Locators.questions_about_important_block)
        )

    @allure.step('Тап на вопрос')
    def click_to_what_is_the_prise(self):
        self.driver.find_element(*Locators.what_is_the_price_question).click()

    @allure.step('Ждем пока откроется ответ')
    def check_what_is_the_prise_answer_visible(self):
        WebDriverWait(self.driver, 5).until(
            expected_conditions.visibility_of_element_located(Locators.what_is_the_price_answer)
        )

    @allure.step('Тап на вопрос')
    def click_to_several_scooters(self):
        self.driver.find_element(*Locators.several_scooters_question).click()

    @allure.step('Ждем пока откроется ответ')
    def check_several_scooters_visible(self):
        WebDriverWait(self.driver, 5).until(
            expected_conditions.visibility_of_element_located(Locators.several_scooters_answer)
        )

    @allure.step('Тап на вопрос')
    def click_to_time_of_rent(self):
        self.driver.find_element(*Locators.time_of_rent_question).click()

    @allure.step('Ждем пока откроется ответ')
    def check_time_of_rent_visible(self):
        WebDriverWait(self.driver, 5).until(
            expected_conditions.visibility_of_element_located(Locators.time_of_rent_answer)
        )

    @allure.step('Тап на вопрос')
    def click_to_order_today(self):
        self.driver.find_element(*Locators.order_today_question).click()

    @allure.step('Ждем пока откроется ответ')
    def check_order_today_visible(self):
        WebDriverWait(self.driver, 5).until(
            expected_conditions.visibility_of_element_located(Locators.order_today_answer)
        )

    @allure.step('Тап на вопрос')
    def click_to_extend_or_return_order(self):
        self.driver.find_element(*Locators.extend_or_return_order_question).click()

    @allure.step('Ждем пока откроется ответ')
    def check_extend_or_return_order_visible(self):
        WebDriverWait(self.driver, 5).until(
            expected_conditions.visibility_of_element_located(Locators.extend_or_return_order_answer)
        )

    @allure.step('Тап на вопрос')
    def click_to_charger(self):
        self.driver.find_element(*Locators.charger_question).click()

    @allure.step('Ждем пока откроется ответ')
    def check_charger_visible(self):
        WebDriverWait(self.driver, 5).until(
            expected_conditions.visibility_of_element_located(Locators.charger_answer)
        )

    @allure.step('Тап на вопрос')
    def click_to_cancel_order(self):
        self.driver.find_element(*Locators.cancel_order_question).click()

    @allure.step('Ждем пока откроется ответ')
    def check_cancel_order_visible(self):
        WebDriverWait(self.driver, 5).until(
            expected_conditions.visibility_of_element_located(Locators.cancel_order_answer)
        )

    @allure.step('Тап на вопрос')
    def click_to_outside_mkad(self):
        self.driver.find_element(*Locators.outside_mkad_question).click()

    @allure.step('Ждем пока откроется ответ')
    def check_outside_mkad_visible(self):
        WebDriverWait(self.driver, 5).until(
            expected_conditions.visibility_of_element_located(Locators.outside_mkad_answer)
        )
