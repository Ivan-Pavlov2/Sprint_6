import allure
from data.data import Urls
from Pages.main_page import MainPage
from locators.main_page_locators import MainPageLocators
from Pages.base_page import BasePage
from locators.order_page_locators import OrderPageLocators

class TestLogoRedirect:

    @allure.title('Тест переход на Яндкс.Дзен')
    @allure.description('При клике на логотип Яндекс в новом окне открывается ссылка на Яндекс.Дзен')
    def test_yandex_logo_redirect(self, driver):
        page = BasePage(driver)
        page.click_to_element(MainPageLocators.YANDEX_LOGO)
        page.wait_for_new_tab(2)
        driver.switch_to.window(driver.window_handles[1])
        page.wait_for_load_page(Urls.dzen_url)
        assert driver.current_url == Urls.dzen_url, f"Failed to redirect to 'https://dzen.ru'"

        @allure.title('Открытие главной страницы при клике на логотип "Самокат"')
        @allure.description('После нажатия на странице заказа на логотип "Самокат"'
                            ', выполнится переход на главную страницу Самоката')
        def test_samokat_logo_redirect(self, driver):
            page = MainPage(driver)
            page.click_to_element(MainPageLocators.ORDER_BUTTON_BIG)
            page.find_my_element(OrderPageLocators.FOR_WHOM_IS_SCOOTER)
            page.click_to_element(MainPageLocators.SAMOKAT_LOGO)
            assert driver.current_url == Urls.main_url, f"Failed to open main page"

