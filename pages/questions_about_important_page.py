from locators.questions_about_important_locators import PageLocators

class QuestionsAaboutImportant:
    def __init__(self, driver):
        self.driver = driver

    def click_question(self, locator):
        # нажатие на вопрос
        self.driver.find_element(*locator).click()

    def get_description_answer(self, locator):
        # проверяет что появился ответ
        return self.driver.find_element(*locator).text
