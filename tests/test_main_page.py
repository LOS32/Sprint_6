import pytest
from pages.main_page import MainPage
from data import questions_and_answers


@pytest.mark.parametrize("num, result", questions_and_answers)
def test_questions_and_answers(driver, num, result):
    # Создаём объект страницы
    main_page = MainPage(driver)

    # Проверяем текст ответа
    assert main_page.get_answer_text(num) == result, f"Ожидалось '{result}', но получено другое"

