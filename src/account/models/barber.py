
from django.db import models


from core.models import BaseModel


class Barber(BaseModel):

    experience_year = models.IntegerField()
    rating = models.FloatField(null=True)
    user = models.OneToOneField(to="account.User",related_name="barber",on_delete=models.CASCADE)

    class Meta:
        ordering = ["-id","-created_at"]
        db_table = "barbers"
        verbose_name = "Барбер"
        verbose_name_plural = "Барберы"