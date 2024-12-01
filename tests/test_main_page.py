import pytest
from pages.main_page import MainPage
from data_questions import questions_and_answers
from conftest import driver

class TestMainPage:

    @pytest.mark.parametrize("num, result", questions_and_answers)
    def test_questions_and_answers(self, driver, num, result):
        main_page = MainPage(driver)
        main_page.open_main_page()
        main_page.click_to_cookie_button()
        main_page.click_to_question(num)
        assert main_page.get_answer_text(num) == result, f"Ожидалось '{result}', но получено другое"

