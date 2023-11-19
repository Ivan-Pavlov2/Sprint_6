import allure
from locators.main_page_locators import MainPageLocators
from Pages.base_page import BasePage

class MainPage(BasePage):
    @allure.step('Прокрутка до кнопки "Заказать"')
    def scroll_to_order_button(self):
        button = self.driver.find_element(*MainPageLocators.ORDER_BUTTON_BIG)
        self.driver.execute_script("arguments[0].scrollIntoView();", button)
        self.find_my_element(MainPageLocators.ORDER_BUTTON_BIG)

    @allure.step('Прокрутка до раздела "Вопросы о важном"')
    def scroll_to_questions(self):
        faq = self.driver.find_element(*MainPageLocators.QUESTIONS)
        self.driver.execute_script("arguments[0].scrollIntoView();", faq)
        self.find_my_element(MainPageLocators.QUESTIONS)

    @allure.step('Кликнуть на вопрос')
    def click_to_question(self, num):
        method, locator = MainPageLocators.QUESTION_LOCATOR
        locator = locator.format(num)
        self.find_my_element((method, locator)).click()

    @allure.step('Получить ответ на вопрос')
    def get_answer(self, num):
        method, locator = MainPageLocators.ANSWER_LOCATOR
        locator = locator.format(num)
        return self.find_my_element((method, locator)).text


