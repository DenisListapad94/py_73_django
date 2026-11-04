from django import forms



from booking_manager.models import Booking

from booking_manager.validators import NameValidator



# class BookingForm(forms.Form):
#     name = forms.CharField(
#         label="наименование",
#         max_length=100,
#         validators=[NameValidator()]
#     )
#     is_active = forms.BooleanField(
#         label="активна",
#         required=False,
#     )
#     visit_time = forms.DateTimeField(label="время записи")
#     description = forms.CharField(
#         label="описание",
#         widget=forms.Textarea(
#             attrs={
#                 "cols": 50,
#                 "rows": 5
#             }
#              ),
#
#     )

class BookingForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["description"].widget.attrs.update({"cols": 50, "rows":5})

    class Meta:
        model = Booking
        fields = ["name","is_active","visit_time","description"]
