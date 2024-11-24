import pytest
import allure
from locators.main_page_locators import MainPageLocators
from pages.main_page import MainPage
from data_questions import URLs
from conftest import driver


@allure.title('Тест на проверку логотипа Самоката')
class TestScooterLogo:
    def test_scooter_logo_redirect(self, driver):
        main_page = MainPage(driver)
        main_page.open_main_page()
        main_page.click_to_cookie_button()
        main_page.click_to_order_button(MainPageLocators.ORDER_BUTTON_HEADER)
        main_page.click_scooter_logo()
        assert driver.current_url == URLs.BASE_URL
