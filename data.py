from helpers import GenerateCustomData
from locators.order_page_locators import OrderPageLocators

questions_and_answers = [
    (0, "Стоимость — 400 рублей в сутки."),
    (1, "Можно сразу несколько самокатов? Конечно! Стоимость каждого нового самоката будет рассчитана отдельно."),
    (2, "Время аренды самоката начинается с момента его получения."),
    (3, "Можно ли заказать самокат прямо на сегодня? Да, если свободные самокаты есть в вашем районе."),
    (4, "Можно ли продлить заказ или вернуть самокат раньше? Да, но только если срок аренды не истёк."),
    (5, "Вы привозите зарядку вместе с самокатом? Да, зарядка идёт в комплекте."),
    (6, "Можно ли отменить заказ? Да, но за 24 часа до даты доставки."),
    (7, "Я живу за МКАДом, привезёте? Да, если ваш адрес находится в зоне доставки."),
]

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
