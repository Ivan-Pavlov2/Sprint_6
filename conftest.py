import pytest
from selenium import webdriver
from locators.main_page_locators import MainPageLocators
import time

@pytest.fixture
def driver():
    firefox_options = webdriver.FirefoxOptions()
    driver = webdriver.Firefox(options=firefox_options)
    driver.set_window_size(1920, 1080)
    driver.get('https://qa-scooter.praktikum-services.ru/')
    driver.find_element(*MainPageLocators.COOKIE_BUTTON).click()
    yield driver
    driver.quit()
