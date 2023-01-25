import django.forms as forms
from .models import Rental
from .models import Reservation, Rental


class ReservationCreateForm(forms.Form):
    """
        ReservationCreateForm is a Django form used for creating reservations.
        It contains fields for selecting a rental, check-in date, and check-out date.
        It also has a clean method to check if the check-in date is before the check-out date.
        """
    rental = forms.ModelChoiceField(Rental.objects.all())
    checkin = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    checkout = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    # add more fields here

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['rental'].required = True
        self.fields['checkin'].required = True
        self.fields['checkout'].required = True

    def clean(self):
        cleaned_data = super().clean()
        checkin = cleaned_data.get("checkin")
        checkout = cleaned_data.get("checkout")
        if checkin and checkout and checkin >= checkout:
            self.add_error('checkin', "Check-in date should be before check-out date.")
            self.add_error('checkout', "Check-out date should be after check-in date.")


class RentalCreateForm(forms.Form):
    """
        RentalCreateForm is a Django form used for creating rentals.
        It contains a field for the rental name.
        """
    name = forms.CharField(max_length=225)
    # add more fields here

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].required = True

