import allure
from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

@allure.title('Тесты на проверку заказа самоката')
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
        # Находим поле для ввода и вводим название станции метро
        self.add_text_to_element(OrderPageLocators.METRO_STATION_DROPDOWN, metro_station)
        # Ожидаем появления первого элемента из выпадающего списка и кликаем на него
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, ".//div[@class='select-search__select']/ul/li[1]/button/div[2]"))).click()

    @allure.step('Заполнение второй страницы формы')
    def fill_second_page(self, date, rental_period, scooter_color):
        self.add_text_to_element(OrderPageLocators.DATE_PICKER_FIELD, date)
        self.click_to_element(OrderPageLocators.DATE_PICKER_FIELD)
        self.click_to_element(rental_period)
        self.click_to_element(scooter_color)

    @allure.step('Клик на кнопку Заказать в форме оформления заказа')
    def confirm_order(self):
        self.click_to_element(OrderPageLocators.CONFIRM_ORDER_BUTTON)

    @allure.step('Проверка наличия на экране кнопки Посмотреть статус')
    def check_order(self):
        return self.find_element_with_wait(OrderPageLocators.VIEW_STATUS_BUTTON).is_displayed()