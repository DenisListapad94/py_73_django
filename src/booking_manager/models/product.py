from django.db import models

from booking_manager.models.managers.product import ProductManager
from core.models import BaseModel


class Product(BaseModel):

    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.PositiveIntegerField()
    amount = models.PositiveIntegerField()

    bookings = models.ManyToManyField(
        to="Booking",
        related_name="products",
        verbose_name="бронирования",
        through="ProductBooking",
    )
    objects = ProductManager()
    class Meta:
        db_table = "products"
        verbose_name = "товар"
        ordering = ["-created_at", "-price", "-amount"]

    def __str__(self):
        return self.name