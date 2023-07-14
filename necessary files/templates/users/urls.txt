from django.urls import path
from users import views

app_name = 'users'

urlpatterns = [   
   path('edit_profile/', views.edit_profile, name='edit_profile'),
   path('booked_rooms/', views.booked_rooms, name='booked_rooms'),

   # ! Admin URLs
   path('admin/all_rooms/', views.all_rooms, name='all_rooms'),
   path('room/delete/<slug:slug>/', views.delete_room, name='delete_room'),
   path('admin/add_room/', views.add_room, name='add_room'),
   path('admin/add_hotel/', views.add_hotel, name='add_hotel'),
   path('admin/edit_room/<slug:slug>/', views.edit_room, name='edit_room'),   

   path('admin/bookings/', views.all_bookings, name='all_bookings'),
   path('cancel_booking/<int:id>/', views.cancel_booking, name='cancel_booking'),
   path('admin/cancel_booking/<int:id>/', views.admin_cancel_booking, name='admin_cancel_booking'),
   path('admin/confirm_booking/<int:id>/', views.admin_confirm_booking, name='admin_confirm_booking'),
   path('admin/complete_booking/<int:id>/', views.admin_complete_booking, name='admin_complete_booking'),


   path('admin/customers/', views.all_customers, name='all_customers'),
   path('admin/feedbacks/', views.all_feedbacks, name='all_feedbacks'),

]