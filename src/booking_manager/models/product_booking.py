from django.db import models

from core.models import BaseModel


class ProductBooking(BaseModel):
    product = models.ForeignKey(to="Product", on_delete=models.CASCADE)
    booking = models.ForeignKey(to="Booking", on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(null=True)
    total_price = models.FloatField(null=True)


    class Meta:
        db_table = "product_bookings"
        verbose_name = "товары в бронировании"
