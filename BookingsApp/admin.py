from django.contrib import admin
from .models import Reservation, Rental

# Register your models here.
admin.site.register(Rental)
admin.site.register(Reservation)
