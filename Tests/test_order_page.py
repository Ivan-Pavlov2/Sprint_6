import allure
from Pages.order_page import OrderPage
from locators.main_page_locators import MainPageLocators
from locators.order_page_locators import OrderPageLocators

class TestOrderPage:
    @allure.title('Оформление заказа по кнопке "Заказать" через шапку страницы')
    def test_create_order_header_order_button(self, driver):
        order = OrderPage(driver)
        order.click_to_element(MainPageLocators.ORDER_BUTTON_IN_HEADER)
        order.fill_form('Иван','Павлов', 'Перово', 'Ул.Новогиреевская д.4', '79000000000')
        order.create_order('20.11.2023', OrderPageLocators.THREE_DAYS, OrderPageLocators.BLACK_CHECKBOX, '')
        text = order.get_success_order_text()
        assert 'Заказ оформлен' in text

    @allure.title('Оформление заказа по кнопке "Заказать" через середину главной страницы')
    def test_create_order_main_order_button(self, driver):
        order = OrderPage(driver)
        order.click_to_element(MainPageLocators.ORDER_BUTTON_BIG)
        order.fill_form('Максим', 'Желтов', 'Студенческая', 'Студенческая улица, 33к8', '79000000001')
        order.create_order('21.11.2023', OrderPageLocators.FIVE_DAYS, OrderPageLocators.GREY_CHECKBOX,
                           'Позвоните за час')
        text = order.get_success_order_text()
        assert 'Заказ оформлен' in text