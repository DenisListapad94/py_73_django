from django.db import models

from booking_manager.constants import CategoryChoices
from core.models import BaseModel


class BookingService(BaseModel):
    category = models.CharField(
        choices=CategoryChoices,
        verbose_name="категория",
        default=CategoryChoices.HAIRCUT
    )
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.PositiveIntegerField()
    duration_minutes = models.PositiveIntegerField()
    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = "booking_services"
        verbose_name = "Услуга"
        ordering = ["-created_at", "-price", "category"]

    def __str__(self):
        return self.name