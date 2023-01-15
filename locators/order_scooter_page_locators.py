from selenium.webdriver.common.by import By


class OrderScooterLocators:
    # локатор кнопки Заказать в хэдере
    order_button_in_header = [By.XPATH, ".//button[@class='Button_Button__ra12g']"]

    # локатор кнопки Заказать в теле страницы
    order_button_in_body = [By.XPATH, ".//button[@class='Button_Button__ra12g Button_Middle__1CSJM']"]

    # локатор поля ввода Имя
    name = [By.XPATH, ".//input[@placeholder='* Имя']"]

    # локатор поля ввода Фамилия
    surname = [By.XPATH, ".//input[@placeholder='* Фамилия']"]

    # локатор поля ввода Адрес
    address = [By.XPATH, ".//input[@placeholder='* Адрес: куда привезти заказ']"]

    # локаторы выбора Стации метро
    metro = [By.XPATH, ".//input[@placeholder='* Станция метро']"]
    metro_selection = [By.XPATH, ".//div[@class='select-search__value']"]
    metro_test_value = [By.XPATH, ".//div[contains(text(),'Бульвар Рокоссовского')]"]

    # локатор поля ввода Телефон
    phone = [By.XPATH, ".//input[@placeholder='* Телефон: на него позвонит курьер']"]

    # локатор кнопки Далее
    next = [By.XPATH, ".//button[contains(text(),'Далее')]"]

    # локатор кнопки Назад
    back = [By.XPATH, ".//button[contains(text(),'Назад')]"]

    # локаторы поля Когда привезти самокат
    date = [By.XPATH, ".//input[@placeholder='* Когда привезти самокат']"]
    date_picker = [By.XPATH, ".//div[@class='react-datepicker__tab-loop']"]
    date_test_value = [By.XPATH, ".//div[contains(text(),'12')]"]

    # локатор поля Срок аренды
    rental_period = [By.XPATH, ".//div[contains(text(),'Срок аренды')]"]
    rental_period_dropdown = [By.XPATH, ".//div[@class='Dropdown-root is-open']"]
    rental_period_test_value = [By.XPATH, ".//div[contains(text(),'сутки')]"]

    # локаторы выбора Цвета самоката
    scooter_color = [By.XPATH, ".//label[contains(text(),'чёрный жемчуг')]"]
    scooter_color_selected = [By.XPATH, ".//div[@class='Order_Checkboxes__3lWSI Order_FilledContainer__2MKAk']"]

    # локатор для поля Комментарий
    comment = [By.XPATH, ".//input[@placeholder='Комментарий для курьера']"]

    # локатор модального окна подтверждения заказа
    approve_order_modal = [By.XPATH, ".//div[@class='Order_Modal__YZ-d3']"]
    # no_button = [By.XPATH, ".//button[contains(text(),'Нет')]"]
    yes_button = [By.XPATH, ".//button[contains(text(),'Да')]"]
    order_successful = [By.XPATH, ".//div[contains(text(),'Заказ оформлен')]"]
    check_status = [By.XPATH, ".//button[contains(text(),'Посмотреть статус')]"]

    # локатор логотипа Самоката
    scooter_header_logo = [By.XPATH, ".//a[@class='Header_LogoScooter__3lsAR']"]

    # локатор логотипа Яндекс
    yandex_header_logo = [By.XPATH, ".//a[@class='Header_LogoYandex__3TSOI']"]

    # локатор лого Учебный тренажер
    study_logo = [By.XPATH, ".//div[contains(text(),'Учебный тренажер')]"]

    # локатор кнопка Яндекса  Найти
    yandex_search = [By.XPATH, ".//button[contains(text(),'Найти')]"]
