from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from users.forms import EditProfileForm
from django.contrib import messages
from account.models import User
from hotel_miramar.models import Booking, Room, Feedback
from hotel_miramar.forms import AddRoomForm, EditRoomForm, AddHotelForm

@login_required
def edit_profile(request):
   if request.method == 'POST':
      edit_profile_form = EditProfileForm(request.POST or None, request.FILES, instance=request.user)
      if edit_profile_form.is_valid():
         edit_profile_form.save()
         messages.success(request, 'Profile updated successfully')
         return redirect('home')
   else:
      edit_profile_form = EditProfileForm(instance=request.user)
   context = {
      'edit_profile_form': edit_profile_form
   }
   return render(request, 'users/edit_profile.html', context)

@login_required
def booked_rooms(request):
   my_bookings = Booking.objects.filter(user=request.user)
   upcoming_bookings = my_bookings.filter(is_active=True)
   cancelled_bookings  = my_bookings.filter(is_cancelled=True)
   completed_bookings = my_bookings.filter(is_completed=True)
   context = {
      'my_bookings': my_bookings,
      'upcoming_bookings': upcoming_bookings,
      'cancelled_bookings': cancelled_bookings,
      'completed_bookings': completed_bookings
   }
   return render(request, 'users/my_booked_rooms.html', context)

@login_required
def cancel_booking(request, id):
   booking = Booking.objects.get(id=id)
   
   if booking.user != request.user:
      messages.warning(request, 'You cannot cancel this booking')
      return redirect('home')
   else:      
      booking.is_active = False
      booking.is_cancelled = True
      room = booking.room
      room.is_booked = False
      room.save()
      booking.save()
      messages.success(request, 'Booking cancelled')
      return redirect(request.META.get('HTTP_REFERER'))
   
@login_required
def admin_cancel_booking(request, id):
   if not request.user.is_staff:
      messages.warning(request, 'You are not authorized to access that page')
      return redirect('home')
   else:      
      booking = Booking.objects.get(id=id)
      booking.is_active = False
      booking.is_cancelled = True
      room = booking.room
      room.is_booked = False
      room.save()
      booking.save()
      messages.success(request, 'Booking cancelled')
      return redirect(request.META.get('HTTP_REFERER'))
   
@login_required
def admin_confirm_booking(request, id):
   if not request.user.is_staff:
      messages.warning(request, 'You are not authorized to access that page')
      return redirect('home')
   else:      
      booking = Booking.objects.get(id=id)
      booking.is_active = True
      booking.is_confirmed = True
      booking.save()
      messages.success(request, 'Booking confirmed')
      return redirect(request.META.get('HTTP_REFERER'))
   
@login_required
def admin_complete_booking(request, id):
   if not request.user.is_staff:
      messages.warning(request, 'You are not authorized to access that page')
      return redirect('home')
   else:      
      booking = Booking.objects.get(id=id)
      booking.is_active = False
      booking.is_confirmed = False
      booking.is_completed = True      
      room = booking.room
      room.is_booked = False
      room.save()
      booking.save()
      messages.success(request, 'Booking completed')
      return redirect(request.META.get('HTTP_REFERER'))

# ! Admin Views
@login_required
def all_rooms(request):
   if not request.user.is_staff:
      messages.warning(request, 'You are not authorized to access that page')
      return redirect('home')
   else:
      all_rooms = Room.objects.all()
      context = {
         'all_rooms': all_rooms
      }
      return render(request, 'users/admin/all_rooms.html', context)

@login_required
def delete_room(request, slug):
   if not request.user.is_staff:
      messages.warning(request, 'You are not authorized to access that page')
      return redirect('home')
   else:
      room = get_object_or_404(Room, slug=slug)
      room.delete()
      messages.success(request, 'Room deleted successfully')
      return redirect(request.META.get("HTTP_REFERER"))  
   
@login_required
def add_room(request):
   if not request.user.is_staff:
      messages.warning(request, 'You are not authorized to access that page')
      return redirect('home')
   else:      
      if request.method == 'POST':
         add_room_form = AddRoomForm(request.POST, request.FILES)
         if add_room_form.is_valid():
            add_room_form.save()
            messages.success(request, 'Room added successfully')
            return redirect('users:all_rooms')
         else:
            messages.error(request, "An error occured")
            return redirect('users:all_rooms')
      else:
         add_room_form = AddRoomForm()   
      context = {
         'add_room_form': add_room_form
      }
      return render(request, 'users/admin/add_room.html', context)
   
@login_required
def add_hotel(request):
   if not request.user.is_staff:
      messages.warning(request, 'You are not authorized to access that page')
      return redirect('home')
   else:      
      if request.method == 'POST':
         add_hotel_form = AddHotelForm(request.POST, request.FILES)
         if add_hotel_form.is_valid():
            add_hotel_form.save()
            messages.success(request, 'New hotel added')
            return redirect('users:all_rooms')
         else:
            messages.error(request, "An error occured")
            return redirect('users:all_rooms')
      else:
         add_hotel_form = AddHotelForm()   
      context = {
         'add_hotel_form': add_hotel_form
      }
      return render(request, 'users/admin/add_hotel.html', context)
   
@login_required
def edit_room(request, slug):
   if not request.user.is_staff:
      messages.warning(request, 'You are not authorized to access that page')
      return redirect('home')
   else:
      room = get_object_or_404(Room, slug=slug)
      if request.method == 'POST':
         edit_room_form = EditRoomForm(
            request.POST or None, request.FILES, instance=room)
         if edit_room_form.is_valid():
            edit_room_form.save()
            messages.success(request, 'Room Updated successfully')
            return redirect('users:all_rooms')
         else:
            messages.error(request, "An error occured")
            return redirect(request.META.get("HTTP_REFERER")) 
      else:
         edit_room_form = EditRoomForm(instance=room)
      context = {
         'room': room,
         'edit_room_form': edit_room_form
      }
      return render(request, 'users/admin/edit_room.html', context)
   
@login_required
def all_bookings(request):
   if not request.user.is_staff:
      messages.warning(request, 'You are not authorized to access that page')
      return redirect('home')
   else:
      all_bookings = Booking.objects.all()
      context = {
         'all_bookings': all_bookings
      }
      return render(request, 'users/admin/all_bookings.html', context)
   

@login_required
def all_customers(request):
   if not request.user.is_staff:
      messages.warning(request, 'You are not authorized to access that page')
      return redirect('home')
   else:      
      all_customers = User.objects.exclude(is_superuser=True)
      context = {
         'all_customers': all_customers
      }
      return render(request, 'users/admin/all_customers.html', context)
   
@login_required
def all_feedbacks(request):
   if not request.user.is_staff:
      messages.warning(request, 'You are not authorized to access that page')
      return redirect('home')
   else:      
      all_feedbacks = Feedback.objects.all()
      context = {
         'all_feedbacks': all_feedbacks
      }
      return render(request, 'users/admin/all_feedbacks.html', context)
