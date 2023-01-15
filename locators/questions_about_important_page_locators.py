from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class QuestionsAboutImportantLocators:
    # локатор блока Важные вопросы
    questions_about_important_block = [By.XPATH, ".//div[@class='Home_FAQ__3uVm4']"]

    # локаторы блока вопроса "Сколько это стоит? И как оплатить?"
    what_is_the_price_question = [By.XPATH, ".//div[contains(text(),'Сколько это стоит? И как оплатить?')]"]
    what_is_the_price_answer = [By.XPATH, ".//p[contains(text(),'Сутки — 400 рублей. Оплата курьеру — наличными или картой.')]"]

    # локаторы блока вопроса "Хочу сразу несколько самокатов! Так можно?"
    several_scooters_question = [By.XPATH, ".//div[contains(text(),'Хочу сразу несколько самокатов! Так можно?')]"]
    several_scooters_answer = [By.XPATH,
                                ".//p[contains(text(),'Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.')]"]

    # локаторы блока вопроса "Как рассчитывается время аренды?"
    time_of_rent_question = [By.XPATH, ".//div[contains(text(),'Как рассчитывается время аренды?')]"]
    time_of_rent_answer = [By.XPATH,
                                ".//p[contains(text(),'Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.')]"]

    # локаторы блока вопроса "Можно ли заказать самокат прямо на сегодня?"
    order_today_question = [By.XPATH, ".//div[contains(text(),'Можно ли заказать самокат прямо на сегодня')]"]
    order_today_answer = [By.XPATH,
                                ".//p[contains(text(),'Только начиная с завтрашнего дня. Но скоро станем расторопнее.')]"]

    # локаторы блока вопроса "Можно ли продлить заказ или вернуть самокат раньше?"
    extend_or_return_order_question = [By.XPATH, ".//div[contains(text(),'Можно ли продлить заказ или вернуть самокат раньше?')]"]
    extend_or_return_order_answer = [By.XPATH,
                                ".//p[contains(text(),'Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.')]"]

    # локаторы блока вопроса "Вы привозите зарядку вместе с самокатом?"
    charger_question = [By.XPATH, ".//div[contains(text(),'Вы привозите зарядку вместе с самокатом?')]"]
    charger_answer = [By.XPATH,
                                ".//p[contains(text(),'Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.')]"]

    # локаторы блока вопроса "Можно ли отменить заказ?"
    cancel_order_question = [By.XPATH, ".//div[contains(text(),'Можно ли отменить заказ?')]"]
    cancel_order_answer = [By.XPATH,
                                ".//p[contains(text(),'Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.')]"]

    # локаторы блока вопроса "Я жизу за МКАДом, привезёте?"
    outside_mkad_question = [By.XPATH, ".//div[contains(text(),'Я жизу за МКАДом, привезёте?')]"]
    outside_mkad_answer = [By.XPATH,
                                ".//p[contains(text(),'Да, обязательно. Всем самокатов! И Москве, и Московской области.')]"]
