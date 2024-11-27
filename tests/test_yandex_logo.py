import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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
        WebDriverWait(driver, 10).until(lambda d: len(d.window_handles) > 1)
        driver.switch_to.window(driver.window_handles[1])
        WebDriverWait(driver, 10).until(EC.url_contains(URLs.DZEN_URL))
        driver.switch_to.window(driver.window_handles[1])
        assert driver.current_url == URLs.DZEN_URL