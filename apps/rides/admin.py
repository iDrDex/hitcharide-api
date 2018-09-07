from django.contrib import admin

from .models import Car, Ride, RideStop, RideBooking, RideComplaint


admin.site.register(RideComplaint)
admin.site.register(Car)
admin.site.register(Ride)
admin.site.register(RideStop)
admin.site.register(RideBooking)
