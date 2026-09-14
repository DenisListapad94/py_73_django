from django.urls import path, re_path

from booking_manager.views import test_view, test_view1

urlpatterns = [
    path('test/', test_view),
    re_path(r"^test1/(?P<username>w+\)/$", test_view1),
]
# /booking_manager/test/