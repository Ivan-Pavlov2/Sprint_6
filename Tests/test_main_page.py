import allure
import pytest
from Pages.main_page import MainPage
from data.data import QuestionsAndAnswers

class TestMainPage:

    @allure.title(
        'Проверка работы выпадающего списка "Вопросы о важном"')
    @allure.description('На главной странице перейти к разделу "Вопросы о важном", нажать на вопрос,'
                        'после этого должен открыться соответствующий ответ')
    @pytest.mark.parametrize('question_number, answer_text', QuestionsAndAnswers.list)
    def test_questions(self, driver, question_number, answer_text):
        main_page = MainPage(driver)
        main_page.scroll_to_questions()
        main_page.click_to_question(question_number)
        text = main_page.get_answer(question_number)
        assert text == answer_text

