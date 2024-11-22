import random
import string
from datetime import datetime, timedelta

class GenerateCastomData:
    def generate_random_name(self):
        return ''.join(random.choice(string.ascii_letters, k=8)).capitalize()

    def generate_random_last_name(self):
        return ''.join(random.choice(string.ascii_letters, k=10)).capitalize()

    def generate_random_phone(self):
        return f"+7{random.randint(9000000000, 9999999999)}"

    def generate_random_address(self):
        streets = ["Ленина", "Невская", "Тверская", "Пушкинская", "Гагарина"]
        house = random.randint(1, 100)
        return f"Улица {random.choice(streets)}, дом {house}"

    def generate_random_date(self, days_from_now=7):
        date = datetime.now() + timedelta(days=random.randint(1, days_from_now))
        return date.strftime("%d.%m.%Y")
