from selenium.webdriver.common.by import By

class PageLocators:
    # Вопросы
    HOW_TO_PAY_QUESTION = (By.ID, "accordion__heading-0")
    MULTIPLE_SCOOTERS_QUESTION = (By.ID, "accordion__heading-1")
    RENTAL_TIME_QUESTION = (By.ID, "accordion__heading-2")
    ORDER_TODAY_QUESTION = (By.ID, "accordion__heading-3")
    EXTEND_ORDER_QUESTION = (By.ID, "accordion__heading-4")
    CHARGER_DELIVERY_QUESTION = (By.ID, "accordion__heading-5")
    CANCEL_ORDER_QUESTION = (By.ID, "accordion__heading-6")
    OUTSIDE_MKAD_QUESTION = (By.ID, "accordion__heading-7")

    # Ответы
    HOW_TO_PAY_ANSWER = (By.ID, "accordion__panel-0")
    MULTIPLE_SCOOTERS_ANSWER = (By.ID, "accordion__panel-1")
    RENTAL_TIME_ANSWER = (By.ID, "accordion__panel-2")
    ORDER_TODAY_ANSWER = (By.ID, "accordion__panel-3")
    EXTEND_ORDER_ANSWER = (By.ID, "accordion__panel-4")
    CHARGER_DELIVERY_ANSWER = (By.ID, "accordion__panel-5")
    CANCEL_ORDER_ANSWER = (By.ID, "accordion__panel-6")
    OUTSIDE_MKAD_ANSWER = (By.ID, "accordion__panel-7")
