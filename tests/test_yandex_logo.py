import allure
from pages.main_page import MainPage
from data_questions import URLs
from conftest import driver


@allure.feature('Логотип Яндекса')
class TestYandexLogo:
    @allure.title('Тест на проверку перехода на страницу Дзен через логотип Яндекс')
    def test_yandex_logo_redirect(self, driver):
        main_page = MainPage(driver)
        main_page.open_main_page()
        main_page.click_to_cookie_button()
        main_page.click_yandex_logo()
        main_page.wait_for_new_window()
        main_page.switch_to_window(1)
        main_page.wait_for_url_contains(URLs.DZEN_URL)
        assert main_page.get_current_url() == URLs.DZEN_URL