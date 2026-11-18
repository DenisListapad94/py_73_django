from django.urls import path
from booking_manager.api.v1.views import BookingViewList, BookingDetailView

urlpatterns = [
    path('books/',BookingViewList.as_view(), name="book_list"),
    path('books/<int:pk>/', BookingDetailView.as_view(), name="book_detail"),
]