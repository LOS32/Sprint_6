import pytest
from pages.main_page import MainPage
from pages.order_page import OrderPage
from locators.main_page_locators import MainPageLocators
from data import order_data

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
        order_page = OrderPage(driver)
        main_page.click_to_element(button_locator)

        order_page.set_order(*order_data[0])

        order_page.click_to_next_button()
        order_page.confirm_order()
        assert order_page.check_order()
