from helpers import GenerateCastomData
from locators.order_page_locators import OrderPageLocators

generator = GenerateCastomData()
order_data = [
    (
        generator.generate_random_name(),
        generator.generate_random_last_name(),
        generator.generate_random_address(),
        "Чистые пруды",  # Название станции метро
        generator.generate_random_phone(),
        generator.generate_random_date(),
        OrderPageLocators.RENTAL_PERIOD_ONE_DAY,
        OrderPageLocators.BLACK_SCOOTER_CHECKBOX
    ),
    (
        generator.generate_random_name(),
        generator.generate_random_last_name(),
        generator.generate_random_address(),
        "Сокольники",  # Название станции метро
        generator.generate_random_phone(),
        generator.generate_random_date(),
        OrderPageLocators.RENTAL_PERIOD_TWO_DAYS,
        OrderPageLocators.GREY_SCOOTER_CHECKBOX
    ),
]
