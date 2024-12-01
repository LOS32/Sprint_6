from selenium.webdriver.common.by import By

class MainPageLocators:
    QUESTION_LOCATOR = (By.XPATH, '//*[@id="accordion__heading-{}"]')
    ANSWER_LOCATOR = (By.XPATH, '//*[@id="accordion__panel-{}"]')
    QUESTION_LOCATOR_TO_SCROLL = (By.XPATH, '//div[@id="accordion__heading-7" and contains(text(), "Я жизу за МКАДом, привезёте?")]')
    ORDER_BUTTON_HEADER = (By.XPATH, "//div[@class='Header_Nav__AGCXC']//button[text()='Заказать']")
    ORDER_BUTTON_MAIN = (By.XPATH, "//div[@class='Home_FinishButton__1_cWm']//button[text()='Заказать']")
    SCOOTER_HEADER_BUTTON = (By.XPATH, "//a[@class='Header_LogoScooter__3lsAR' and @href='/']")
    YANDEX_HEADER_BUTTON = (By.XPATH, "//a[@class='Header_LogoYandex__3TSOI' and @href='//yandex.ru']")
    COOKIE_BUTTON = (By.XPATH, "//button[@id='rcc-confirm-button']")


