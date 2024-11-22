from helpers import GenerateCustomData
from locators.order_page_locators import OrderPageLocators

generator = GenerateCustomData()
order_data = [
    (
        generator.generate_random_name(),
        generator.generate_random_last_name(),
        generator.generate_random_address(),
        OrderPageLocators.METRO_STATION_CLEAN_PONDS,
        generator.generate_random_phone(),
        generator.generate_random_date(),
        OrderPageLocators.RENTAL_PERIOD_ONE_DAY,
        OrderPageLocators.BLACK_SCOOTER_CHECKBOX
    ),
    (
        generator.generate_random_name(),
        generator.generate_random_last_name(),
        generator.generate_random_address(),
        OrderPageLocators.METRO_STATION_SOKOLNIKI,
        generator.generate_random_phone(),
        generator.generate_random_date(),
        OrderPageLocators.RENTAL_PERIOD_TWO_DAYS,
        OrderPageLocators.GREY_SCOOTER_CHECKBOX
    ),
]