import allure
from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage

@allure.feature('Оформление заказа')
class OrderPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Отрытие главной страницы')
    def open_main_page(self):
        self.open_page(URLs.BASE_URL)

    @allure.step('Заполнение первой страницы формы')
    def fill_first_page(self, name, last_name, address, metro_locator, phone):
        self.add_text_to_element(OrderPageLocators.ORDER_NAME_FIELD, name)
        self.add_text_to_element(OrderPageLocators.ORDER_LAST_NAME_FIELD, last_name)
        self.add_text_to_element(OrderPageLocators.ADDRESS_FIELD, address)
        self.select_metro_station(metro_locator)
        self.add_text_to_element(OrderPageLocators.PHONE_FIELD, phone)

    @allure.step('Клик на кнопку Далее в форме оформления заказа')
    def click_to_next_button(self):
        self.click_to_element(OrderPageLocators.NEXT_BUTTON)

    @allure.step('Выбор станции метро')
    def select_metro_station(self, metro_station):
        self.add_text_to_element(OrderPageLocators.METRO_STATION_DROPDOWN, metro_station)
        self.wait_for_element_visible(OrderPageLocators.METRO_STATION_SAMPLE)
        self.click_to_element(OrderPageLocators.METRO_STATION_SAMPLE)

    @allure.step('Заполнение второй страницы формы')
    def fill_second_page(self, date, rental_period_label, scooter_color):
        self.click_to_element(OrderPageLocators.DATE_PICKER_FIELD)
        self.add_text_to_element(OrderPageLocators.DATE_PICKER_FIELD, date)
        self.select_order_date(date)
        self.select_rental_period(rental_period_label)
        self.click_to_element(scooter_color)

    @allure.step('Выбор даты заказа')
    def select_order_date(self, order_date):
        day, month, year = order_date.split('.')
        self.click_to_element(OrderPageLocators.DATE_PICKER_FIELD)
        date_locator = (
            OrderPageLocators.DATE_PICKER_TEMPLATE[0],
            OrderPageLocators.DATE_PICKER_TEMPLATE[1].format(day)
        )
        self.wait_for_element_visible(date_locator)
        self.click_to_element(date_locator)

    @allure.step('Выбор периода аренды')
    def select_rental_period(self, rental_period_label):
        self.click_to_element(OrderPageLocators.RENTAL_PERIOD_DROPDOWN)
        rental_period_locator = self.format_locators(OrderPageLocators.RENTAL_PERIOD_TEMPLATE, rental_period_label)
        self.wait_for_element_visible(rental_period_locator)
        self.click_to_element(rental_period_locator)

    @allure.step('Оформление заказа')
    def confirm_order(self):
        self.click_to_element(OrderPageLocators.ORDER_BUTTON)
        self.click_to_element(OrderPageLocators.CONFIRM_ORDER_BUTTON)

    @allure.step('Проверка отображения кнопки "Посмотреть статус"')
    def check_order(self):
        return self.find_element_with_wait(OrderPageLocators.VIEW_STATUS_BUTTON).is_displayed()

