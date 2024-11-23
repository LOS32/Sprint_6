import pytest
from pages.order_page import OrderPage
from pages.main_page import MainPage
from locators.main_page_locators import MainPageLocators
from data_orders import order_data
from conftest import driver

class TestOrderPage:

    @pytest.mark.parametrize(
        "button_locator, order_data",
        [
            (MainPageLocators.ORDER_BUTTON_HEADER, order_data[0]),
            (MainPageLocators.ORDER_BUTTON_MAIN, order_data[1]),
        ]
    )
    def test_create_order(self, driver, button_locator, order_data):
        main_page = MainPage(driver)
        main_page.open_main_page()
        main_page.click_to_cookie_button()
        main_page.click_to_order_button(button_locator)

        order_page = OrderPage(driver)
        order_page.fill_first_page(*order_data[:5])
        order_page.click_to_next_button()
        order_page.fill_second_page(*order_data[5:])
        order_page.confirm_order()
        assert order_page.check_order()
