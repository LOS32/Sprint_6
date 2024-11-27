import allure
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage
from data_questions import URLs

@allure.title('Тесты на проверку вопросов')
class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Отрытие главной страницы')
    def open_main_page(self):
        self.open_page(URLs.BASE_URL)

    @allure.step('Клик на кнопку принятия куки')
    def click_to_cookie_button(self):
        self.click_to_element(MainPageLocators.COOKIE_BUTTON)

    @allure.step('Клик на вопрос')
    def click_to_question(self, num):
        locator_to_scroll = MainPageLocators.QUESTION_LOCATOR_TO_SCROLL
        locator_q_formatted = self.format_locators(MainPageLocators.QUESTION_LOCATOR, num)
        self.scroll_to_element(locator_to_scroll)
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

    @allure.step('Клик на кнопку заказа')
    def click_to_order_button(self, locator):
        self.click_to_element(locator)

    @allure.step('Клик на логотип "Самокат"')
    def click_scooter_logo(self):
        self.click_to_element(MainPageLocators.SCOOTER_HEADER_BUTTON)

    @allure.step('Клик на логотип "Яндекс"')
    def click_yandex_logo(self):
        self.click_to_element(MainPageLocators.YANDEX_HEADER_BUTTON)







