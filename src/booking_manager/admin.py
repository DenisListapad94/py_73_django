from django.contrib import admin

from account.models import Barber
from .models import Booking, BookingService, Product


# Register your models here.



class EmailExistBarberListFilter(admin.SimpleListFilter):
    # Human-readable title which will be displayed in the
    # right admin sidebar just above the filter options.
    title = "Заведена ли почта у барбера"

    # Parameter for the filter that will be used in the URL query.
    parameter_name = "email_barber_exist"

    def lookups(self, request, model_admin):
        """
        Returns a list of tuples. The first element in each
        tuple is the coded value for the option that will
        appear in the URL query. The second element is the
        human-readable name for the option that will appear
        in the right sidebar.
        """
        return [
            ("exist", "barber email exist"),
            ("not exist", "barber not email exist"),
        ]

    def queryset(self, request, queryset):
        """
        Returns the filtered queryset based on the value
        provided in the query string and retrievable via
        `self.value()`.
        """
        # Compare the requested value (either '80s' or '90s')
        # to decide how to filter the queryset.
        if self.value() == "exist":
            return queryset.filter(barber__user__email__isnull=False)
        if self.value() == "not exist":
            return queryset.filter(barber__user__email__isnull=True)


class ProductInline(admin.TabularInline):
    model = Product.bookings.through


@admin.register(Booking)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ("name", "is_active", "visit_time","created_at","barber_email")
    fields = ["name", "is_active","visit_time","booking_service",("barber","client")]
    list_editable = ("is_active",)
    list_display_links = ("name","barber_email",)
    list_filter  = ("visit_time","is_active",EmailExistBarberListFilter)
    ordering = ("-visit_time",)
    search_fields = ("name",)
    list_per_page = 3
    inlines = [
        ProductInline
    ]
    actions = ["make_is_active","make_last_barber"]

    @admin.action(description="Mark selected statis is activated")
    def make_is_active(self,request, queryset):
        queryset.update(is_active=True)


    @admin.action(description="Mark selected edit last barber")
    def make_last_barber(self,request, queryset):
        barber = Barber.objects.last()
        queryset.update(barber=barber)

    # fieldsets = [
    #     (
    #         None,
    #         {
    #             "fields": ["name", "is_active", "visit_time"],
    #         },
    #     ),
    #     (
    #         "Advanced options",
    #         {
    #             "classes": ["collapse"],
    #             "fields": ["barber","client"],
    #         },
    #     ),
    # ]
    # exclude = ["is_active"]


    @admin.display(empty_value="???")
    def barber_email(self, obj):
        if obj.barber:
            return obj.barber.user.email



class BookingInline(admin.StackedInline):
    model = Booking
    extra = 0


@admin.register(BookingService)
class BookingServiceAdmin(admin.ModelAdmin):
    inlines = [
        BookingInline,
    ]


# @admin.register(Product)
# class ProductAdmin(admin.ModelAdmin):
#
#     filter_horizontal = ["bookings"]