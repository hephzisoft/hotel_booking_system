from django.contrib import admin
from hotel_miramar.models import Hotel, Room, Booking, Enquiry, Feedback


admin.site.register(Enquiry)
admin.site.register(Hotel)
admin.site.register(Room)
admin.site.register(Booking)
admin.site.register(Feedback)