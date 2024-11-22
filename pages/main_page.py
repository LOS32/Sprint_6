import allure

from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage
from data_questions import URLs


@allure.title('Тесты на проверку вопросов')
class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def open_main_page(self):
        self.open_page(URLs.BASE_URL)

    @allure.step('Клик на вопрос')
    def click_to_question(self, num):
        locator_q_formatted = self.format_locators(MainPageLocators.QUESTION_LOCATOR, num)
        self.scroll_to_element(MainPageLocators.QUESTION_LOCATOR_TO_SCROLL)
        self.click_to_element(locator_q_formatted)

    @allure.step('Получение ответа на вопрос')
    def get_answer_text(self, num):
        #Нажимает на вопрос и возвращает текст ответа
        locator_a_formatted = self.format_locators(MainPageLocators.ANSWER_LOCATOR, num)
        return self.get_text_from_element(locator_a_formatted)

    @allure.step('Проверка ответа')
    def check_question_and_answer(self, num):
        self.click_to_question(num)
        return self.get_answer_text(num)


