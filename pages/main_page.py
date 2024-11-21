from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage

class QuestionsAaboutImportant:
    def __init__(self, driver):
        self.driver = driver

    def click_question(self, locator):
        # нажатие на вопрос
        self.driver.find_element(*locator).click()

    def get_description_answer(self, locator_q, locator_a, num):
        #Нажимает на вопрос и возвращает текст ответа
        locator_q_formatted = self.format_locators(locator_q, num)
        locator_a_formatted = self.format_locators(locator_a, num)
        self.click_to_element(locator_q_formatted)
        return self.get_text_from_element(locator_a_formatted)
