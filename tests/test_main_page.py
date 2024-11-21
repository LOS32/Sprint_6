import pytest
from pages.main_page import MainPage
from locators.main_page_locators import MainPageLocators

@pytest.mark.parametrize("num, result", [
    (0, "Стоимость — 400 рублей в сутки."),
    (1, "Ответ на вопрос 2"),
    # Добавь другие вопросы и ответы
])
def test_questions_and_answers(driver, num, result):
    # Создаём объект страницы
    main_page = MainPage(driver)

    # Проверяем текст ответа
    assert main_page.get_answer_text(
        MainPageLocators.QUESTION_LOCATOR,
        MainPageLocators.ANSWER_LOCATOR,
        num
    ) == result, f"Ожидалось '{result}', но получено другое"
