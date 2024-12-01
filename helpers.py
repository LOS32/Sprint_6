import random
from datetime import datetime, timedelta

class GenerateCastomData:
    def generate_random_name(self):
        names = ["Иван", "Петр", "Алексей", "Сергей", "Федор"]
        return random.choice(names)

    def generate_random_last_name(self):
        last_names = ["Иванов", "Петров", "Алексеев", "Сергеев", "Федоров"]
        return random.choice(last_names)

    def generate_random_phone(self):
        return f"+7{random.randint(9000000000, 9999999999)}"

    def generate_random_address(self):
        streets = ["Ленина", "Невская", "Тверская", "Пушкинская", "Гагарина"]
        house = random.randint(1, 100)
        return f"Улица {random.choice(streets)}, дом {house}"

    def generate_random_date(self, days_from_now=4):
        delta_days = random.randint(1, days_from_now)
        date = datetime.now() + timedelta(delta_days)
        return date.strftime("%d.%m.%Y")
