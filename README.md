## Финальный проект 4 спринта Отчеты о тестировании Яндекс Практикум
В проекте реализованы UI-тесты на Silenium и Python с паттерном проектирования Page Object Model (POM) и фреймворком генерации отчетов о тестировании Allure для сайта https://qa-scooter.praktikum-services.ru/

### Список реализованных UI тестов:
Чтобы просмотреть отчет о тестировании и тест-кейсы, находясь в корне проекта можно выполнить команду: 
>>allure serve allure_results

### Запуск
Для запуска необходимы python3, allure, selenium, pytest и webDriver для Firefox (в Google Chrome не отрабатывает позитивный флоу подтверждения заказа).

Для запуска:
>>pytest --alluredir=allure_results    