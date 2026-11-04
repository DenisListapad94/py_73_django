from django.apps import AppConfig
from django.db.models.signals import post_save

class BookingManagerConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'booking_manager'
    verbose_name = "Менеджер бронирований"
    verbose_name_plural = "Менеджер бронирований"

    def ready(self):

        from booking_manager.signals import signal_post_save_booking_with_service_1
        post_save.connect(signal_post_save_booking_with_service_1,self)





