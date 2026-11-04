import transaction
from django.db.models.signals import post_save
from django.dispatch import receiver

from booking_manager.models import Booking, Product
from django.db import transaction


@transaction.atomic
@receiver(post_save, sender=Booking)
def signal_post_save_booking_with_service_1(sender, instance, created, **kwargs):
    products = Product.objects.filter(id__gte=75, id__lte=76).values_list("id", flat=True)
    instance_booking_service = instance.booking_service
    if instance_booking_service and instance.booking_service.id == 2:
        if created:
            instance.products.add(*products)
        else:
            instance.products.set(products)
