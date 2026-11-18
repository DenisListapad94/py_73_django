from django.urls import path, re_path, include

from booking_manager.views import AboutPageView, home, BookingListView, BookCreateView, book_form

urlpatterns = [
    path('about/', AboutPageView.as_view(), name="about"),
    path('book/', BookingListView.as_view(), name="book"),
    path('home/', home, name="homepage"),
    path("book_form/", book_form, name="book_form"),
    path("api/", include("booking_manager.api.urls")),
    # path("new_view/",MyView.as_view())
    # re_path(r"^test1/(?P<username>w+\)/$", test_view1),
]
# /booking_manager/test/