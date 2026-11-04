from random import randint, choice

from django.core.management.base import BaseCommand

from booking_manager.models import Product, Booking


class Command(BaseCommand):

    def handle(self, *args, **options):
        products = Product.objects.all()
        for booking in Booking.objects.all():
            for i in range(1, randint(2,5)):
                booking.products.add(choice(products))
        self.stdout.write(self.style.SUCCESS("New products created"))