from django.urls import path, re_path

from booking_manager.views import about, booking, home

urlpatterns = [
    path('about/', about, name="about"),
    path('book/', booking, name="book"),
    path('home/<int:home>', home, name="homepage"),
    # re_path(r"^test1/(?P<username>w+\)/$", test_view1),
]
# /booking_manager/test/