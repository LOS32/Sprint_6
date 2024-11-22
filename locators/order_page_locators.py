from selenium.webdriver.common.by import By

class OrderPageLocators:
    ORDER_NAME_FIELD = (By.XPATH, "//input[contains(@placeholder, 'Имя')]")
    ORDER_LAST_NAME_FIELD = (By.XPATH, "//input[@placeholder='* Фамилия']")
    NEXT_BUTTON = (By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM' and text()='Далее']")
    ORDER_BUTTON = (By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM' and text()='Заказать']")
    CONFIRM_ORDER_BUTTON = (By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM' and text()='Да']")
    VIEW_STATUS_BUTTON = (By.XPATH, "//div[@class='Order_NextButton__1_rCA']//button[text()='Посмотреть статус']")
    ADDRESS_FIELD = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    METRO_STATION_DROPDOWN = (By.XPATH, "//input[@placeholder='* Станция метро']")
    METRO_STATION_CLEAN_PONDS = (By.XPATH, "//input[@value='Чистые пруды']")
    METRO_STATION_SOKOLNIKI = (By.XPATH, "//input[@value='Сокольники']")
    PHONE_FIELD = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    DATE_PICKER_FIELD = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    RENTAL_PERIOD_FIELD = (By.XPATH, "//div[@class='Dropdown-control' and .//div[text()='* Срок аренды']]")
    RENTAL_PERIOD_ONE_DAY = (By.XPATH, "//div[@class='Dropdown-placeholder is-selected' and text()='сутки']")
    RENTAL_PERIOD_TWO_DAYS = (By.XPATH, "//div[@class='Dropdown-placeholder is-selected' and text()='двое суток']")
    BLACK_SCOOTER_CHECKBOX = (By.XPATH, "//input[@id='black']")
    GREY_SCOOTER_CHECKBOX = (By.XPATH, "//input[@id='grey']")






