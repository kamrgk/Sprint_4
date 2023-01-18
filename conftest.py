import pytest
from selenium import webdriver


@pytest.fixture
def driver_init(request):
    driver = webdriver.Firefox()
    request.cls.driver = driver
    driver.maximize_window()
    driver.get("https://qa-scooter.praktikum-services.ru/")

    yield
    driver.quit()