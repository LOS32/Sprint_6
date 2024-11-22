import allure

from locators.main_page_locators import MainPageLocators
from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage

@allure.title('Тесты на проверку заказа самоката')
class OrderPage(BasePage):

    @allure.step('Клик на кнопку заказать в заголовке главной страницы')
    def set_order(self, name, last_name, address, metro_locator, phone, date, rental_period, scooter_color):
        self.add_text_to_element(OrderPageLocators.ORDER_NAME_FIELD, name)
        self.add_text_to_element(OrderPageLocators.ORDER_LAST_NAME_FIELD, last_name)
        self.add_text_to_element(OrderPageLocators.ADDRESS_FIELD, address)
        self.click_to_element(OrderPageLocators.METRO_STATION_DROPDOWN)
        self.click_to_element(metro_locator)
        self.add_text_to_element(OrderPageLocators.PHONE_FIELD, phone)
        self.click_to_element(OrderPageLocators.NEXT_BUTTON)
        self.add_text_to_element(OrderPageLocators.DATE_PICKER_FIELD, date)
        self.click_to_element(rental_period)
        self.click_to_element(scooter_color)

    @allure.step('Клик на кнопку Далее в форме оформления заказа')
    def click_to_next_button(self):
        self.click_to_element(OrderPageLocators.NEXT_BUTTON)

    @allure.step('Клик на кнопку Заказать в форме оформления заказа')
    def confirm_order(self):
        self.click_to_element(OrderPageLocators.CONFIRM_ORDER_BUTTON)

    @allure.step('Проверка наличия на экране кнопки Посмотреть статус')
    def check_order(self):
        return self.find_element_with_wait(OrderPageLocators.VIEW_STATUS_BUTTON).is_displayed()