from django.urls import path, re_path

from booking_manager.views import AboutPageView, home, BookingListView, BookCreateView

urlpatterns = [
    path('about/', AboutPageView.as_view(), name="about"),
    path('book/', BookingListView.as_view(), name="book"),
    path('home/', home, name="homepage"),
    path("book_form/", BookCreateView.as_view(), name="book_form"),
    # path("new_view/",MyView.as_view())
    # re_path(r"^test1/(?P<username>w+\)/$", test_view1),
]
# /booking_manager/test/