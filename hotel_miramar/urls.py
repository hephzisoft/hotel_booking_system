from django.urls import path
from hotel_miramar.views import home, about, contact, rooms, room_details, search_rooms

urlpatterns = [
   path('', home, name='home'),
   path('rooms/', rooms, name='rooms'),
   path('room/<slug:slug>/', room_details, name='room_details'),
   path('search/', search_rooms, name='search'),
   path('about/', about, name='about'),
   path('contact/', contact, name='contact')
]