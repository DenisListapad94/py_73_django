from django.db import models


class BookingQuerySet(models.QuerySet):
    pass


class BookingManager(models.Manager):
    def get_queryset(self):
        return BookingQuerySet(self.model, using=self._db)

    def all_optimize(self):
        return (
            self.get_queryset()
            .prefetch_related(
                "products"
            )
            .select_related(
                "client__user",
                "barber__user"
            )
        )