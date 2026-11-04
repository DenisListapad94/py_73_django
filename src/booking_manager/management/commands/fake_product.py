from random import randint
from faker import Faker
from django.core.management.base import BaseCommand

from booking_manager.models import Product


fake = Faker("ru_RU")
class Command(BaseCommand):

    def handle(self, *args, **options):
        product_names = [
            "Шампунь для волос",
            "Масло для бороды",
            "Бальзам для бороды",
            "Воск для усов",
            "Помада для укладки",
            "Глина для волос",
            "Матовая паста",
            "Гель для волос",
            "Спрей для укладки",
            "Тоник для волос",
            "Крем для бритья",
            "Лосьон после бритья",
            "Одеколон",
            "Расческа для бороды",
            "Щетка для бороды",
        ]
        products = []
        if not Product.objects.exists():
            for name in product_names:
                products.append(
                    Product(
                        name=name,
                        description=fake.text(max_nb_chars=150),
                        price=randint(10, 100) * 10,
                        amount=randint(0, 100),
                    )
                )

            Product.objects.bulk_create(products)
        self.stdout.write(self.style.SUCCESS("New products created"))