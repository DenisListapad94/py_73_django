
from django.db import models



class ProductQuerySet(models.QuerySet):

    def annotate_product_count(self):
        self.filter().annotate(
            count_bookings=models.Count("bookings")
        ).filter(
             count_bookings__gte=2,
             price__gte=models.Avg("price")
        ).count()



class ProductManager(models.Manager):
    def get_queryset(self):
        return ProductQuerySet(self.model, using=self._db)

    def annotate_product_count(self):
        return self.get_queryset().annotate_product_count()


