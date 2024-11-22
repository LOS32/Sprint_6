import pytest

from conftest import driver
from locators.main_page_locators import MainPageLocators
from pages.main_page import MainPage
from data import order_data

class TestOrderPage:

    @pytest.mark.parametrize(
        'locator', 'order_data',
        [
            (MainPageLocators.ORDER_BUTTON_MAIN.data.ORDER_DATA_1),
            (OrderPageLocators.ORDER_BUTTON_HEADER.data.ORDER_DATA_2),
        ]
    )
    def test_create_order(self, driver, locator, order_data):
    main_page = MainPage(driver)
    oreder_page = OrderPage(driver)
    main_page.click_to_next_button(locator)
    oreder_page.set_order()
    assert oreder_page.check_order

