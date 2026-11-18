import time

from django.shortcuts import render, HttpResponse, HttpResponseRedirect,reverse

from booking_manager.forms import BookingForm
from booking_manager.models import Booking
from django.conf import settings
from django.core.cache import caches
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.contrib.auth.decorators import permission_required, login_required
from django.db import transaction
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.views.decorators.cache import cache_page
from django.urls import reverse_lazy
from django.views.generic.edit import FormView
# @cache_page(settings.CACHE_TIMEOUT)
@transaction.atomic
def booking(request):


    # import time
    # time.sleep(10)
    template_name = "booking.html"

    # Booking.objects.filter(id__gte=4,id__lte=10).select_for_update(skip_locked=True)
    # print("ho")
    # for i in range(60):
    #     print(i)
    #     time.sleep(1)
    # raise
    # import pdb;pdb.set_trace()
    # raise
    context = {
        "bookings": Booking.objects.all_optimize()
    }
    return render(request, template_name=template_name,context=context)

class BookingListView(ListView):
    template_name = "booking.html"
    model = Booking
    queryset = Booking.objects.all_optimize()

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context["bookings"] = self.queryset
    #     return context


from django.views import View


# class MyView(View):
#     def get(self, request, *args, **kwargs):
#         return HttpResponse("<h1>GET HELLO</h1>")
#
#     def post(self, request, *args, **kwargs):
#         return HttpResponse("<h1>POST HELLO</h1>")

# def new_test_view(request):
#     return HttpResponse("<h1>HELLO</h1>")



class AboutPageView(TemplateView):
    template_name = "about.html"

# def about(request):
#     template_name = "about.html"
#     return render(request, template_name=template_name)



@login_required(login_url="/admin/login")
# @permission_required(
#     perm="booking_manager.view_client",
#     login_url="/admin/login",
#     raise_exception =True,
#)
def home(request):
    template_name = "home.html"
    return render(request, template_name=template_name)



class BookCreateView(LoginRequiredMixin,PermissionRequiredMixin,FormView):
    login_url="/admin/login"
    template_name = "booking_form.html"
    form_class = BookingForm
    success_url =  reverse_lazy("book")
    permission_required = "booking_manager.add_booking"
    redirect_field_name = reverse_lazy("book")


def book_form(request):
    template_name = "booking_form.html"

    if request.method == "POST":

        # create a form instance and populate it with data from the request:
        form = BookingForm(request.POST,request.FILES)

        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:

            form.save()
            # caches["default"].clear()
            return HttpResponseRedirect(reverse("book"))

    else:
        form = BookingForm()

    context = { "form": form}

    return render(request, template_name=template_name,context=context)