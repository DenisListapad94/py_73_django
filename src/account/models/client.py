
from django.db import models

from account.constants import ClientStatusChoices
from core.models import BaseModel


class Client(BaseModel):

    status = models.CharField(choices=ClientStatusChoices, default=ClientStatusChoices.NOOB)
    date_of_birth = models.DateField(null=True)
    user = models.OneToOneField(to="account.User",related_name="client",on_delete=models.CASCADE)

    class Meta:
        ordering = ["-id","-created_at"]
        db_table = "clients"
        verbose_name = "Клиент"
        verbose_name_plural = "Клиенты"