from datetime import datetime

from django.db import models

from booking_manager.models.managers.booking import BookingManager
from booking_manager.validators import NameValidator
from core.models import BaseModel


class Booking(BaseModel):
    name = models.CharField(
        max_length=30,
        verbose_name="наименование",
        unique=True,
        # validators=[NameValidator]
    )
    is_active = models.BooleanField(
        default=True,
        verbose_name="активна"
    )
    visit_time = models.DateTimeField(
        verbose_name="время визита",
        null=True,
        blank=True,
        default=datetime.now()
    )
    photo = models.ImageField(null=True,upload_to="")

    booking_service = models.ForeignKey(
        to="BookingService",
        on_delete=models.SET_NULL,
        related_name="bookings",
        verbose_name="услуги",
        null=True,
    )
    description = models.CharField(
        verbose_name="описание",
        null=True,
        blank=True,
    )

    barber = models.ForeignKey(to="account.Barber",related_name="bookings",on_delete=models.SET_NULL,null=True,blank=True)
    client = models.ForeignKey(to="account.Client", related_name="bookings", on_delete=models.SET_NULL, null=True,blank=True)
    objects = BookingManager()

    class Meta:
        db_table = "bookings"
        verbose_name = "Бронирование мастера"
        verbose_name_plural = "Бронирования мастеров"
        ordering = ["-created_at","name"]

    def __str__(self):
        return self.name




