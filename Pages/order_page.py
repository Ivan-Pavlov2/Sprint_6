import allure
from locators.order_page_locators import OrderPageLocators
from selenium.webdriver.common.keys import Keys
from Pages.base_page import BasePage

class OrderPage(BasePage):

    @allure.step('Заполнить "Имя"')
    def set_name(self, name):
        self.set_text_to_element(OrderPageLocators.NAME_FIELD, name)

    @allure.step('Заполнить "Фамилия"')
    def set_last_name(self, last_name):
        self.set_text_to_element(OrderPageLocators.LAST_NAME_FIELD, last_name)

    @allure.step('Заполнить адрес')
    def set_address(self, address):
        self.set_text_to_element(OrderPageLocators.ADDRESS_INPUT, address)

    @allure.step('Выбрать станцию метро')
    def set_metro(self, metro):
        self.set_text_to_element(OrderPageLocators.METRO_STATION_INPUT, metro)
        self.click_to_element(OrderPageLocators.METRO_STATION_LIST)
        self.check_invisibility(OrderPageLocators.METRO_STATION_LIST)

    @allure.step('Указать номер телефона')
    def set_phone_number(self, phone_number):
        self.set_text_to_element(OrderPageLocators.PHONE_INPUT, phone_number)

    @allure.step('Нажать на кнопку "Далее"')
    def click_next_button(self):
        self.click_to_element(OrderPageLocators.NEXT_BUTTON)

    @allure.step('Заполнить форму "Для кого самокат?"')
    def fill_form(self, name, last_name, metro, address, phone_number):
        self.set_name(name)
        self.set_last_name(last_name)
        self.set_address(address)
        self.set_metro(metro)
        self.set_phone_number(phone_number)
        self.click_next_button()

    @allure.step('Выбрать дату, когда привезти самокат')
    def set_date(self, date):
        self.set_text_to_element(OrderPageLocators.DATE_FIELD, date)
        self.find_my_element(OrderPageLocators.CALENDAR)
        self.set_text_to_element(OrderPageLocators.DATE_FIELD, Keys.ENTER)
        self.check_invisibility(OrderPageLocators.CALENDAR)

    @allure.step('Выбрать срок аренды самоката')
    def select_rental_period(self, period):
        self.click_to_element(OrderPageLocators.RENT_TIME_LIST)
        self.click_to_element(period)

    @allure.step('Выбрать цвет самоката')
    def set_color(self, color):
        self.click_to_element(color)

    @allure.step('Добавить комментарий')
    def set_comment(self, comment):
        self.set_text_to_element(OrderPageLocators.COMMENT_FIELD, comment)

    @allure.step('Нажать на кнопку "Заказать"')
    def click_to_order_button(self):
        self.click_to_element(OrderPageLocators.ORDER_BUTTON_IN_HEADER)

    @allure.step('Клик по кнопке "Да"')
    def click_confirmation_order(self):
        self.click_to_element(OrderPageLocators.YES_BUTTON)
        self.check_invisibility(OrderPageLocators.YES_BUTTON)

    @allure.step('Проверка всплывающего окна с номером заказа')
    def get_success_order_text(self):
        text = self.find_my_element(OrderPageLocators.ORDER_SUCCESS_WINDOW).text
        return text

    @allure.step('Заполнить форму "Про аренду" и создать заказ')
    def create_order(self, date, period, color, comment):
        self.set_date(date)
        self.select_rental_period(period)
        self.set_color(color)
        self.set_comment(comment)
        self.click_to_order_button()
        self.click_confirmation_order()
