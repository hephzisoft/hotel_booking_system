from django.shortcuts import render, redirect
from hotel_miramar.models import Enquiry
from django.contrib import messages
from hotel_miramar.models import Room, Feedback
from hotel_miramar.forms import BookingForm, FeedBackForm
from django.db.models import Q

# Create your views here.
def home(request):
   all_feedbacks = Feedback.objects.all()
   context = {
      'all_feedbacks': all_feedbacks
   }
   return render(request, 'hotel_miramar/home.html', context)

def about(request):
   return render(request, 'hotel_miramar/about.html')

def rooms(request):
   rooms = Room.objects.all()   
   context = {
      'rooms': rooms
   }
   return render(request, 'hotel_miramar/rooms.html', context)

def room_details(request, slug):
   room = Room.objects.get(slug=slug)

   if request.method == "POST":
      booking_form = BookingForm(request.POST)
      feedback_form = FeedBackForm(request.POST)

      if feedback_form.is_valid():
         instance = feedback_form.save(commit=False)
         instance.user = request.user
         instance.room = room
         instance.save()
         messages.success(request, 'Feedback complete, thank you 🙂')
         return redirect('room_details', slug=slug)

      if booking_form.is_valid():
         instance = booking_form.save(commit=False)
         instance.user = request.user
         instance.room = room
         instance.is_active = True
         instance.save()
         messages.success(request, f'Your have successfully booked {room.name}!')
         return redirect('room_details', slug=slug)
      
   else:      
      booking_form = BookingForm()
      feedback_form = FeedBackForm()

   context = {
      'room': room,
      'booking_form': booking_form,
      'feedback_form': feedback_form
   }
   return render(request, 'hotel_miramar/room_details.html', context)

def search_rooms(request):
   if 'key' in request.GET:
      querystring=request.GET['key']
      if querystring:
         rooms = Room.objects.filter(
            Q(name__icontains=querystring) |
            Q(hotel__name__icontains=querystring) |
            Q(room_options__icontains=querystring) |
            Q(price__icontains=querystring)         
         )
         if rooms:
            context = {
               'rooms': rooms,    
               'querystring': querystring
            }
            return render(request, 'hotel_miramar/search_results.html', context)
         else:
            return render(request, 'hotel_miramar/search_results.html')
      else:
         messages.error(request, 'Please enter a search item!')
         return redirect('home')  
   else:
      messages.error(request, 'Please enter a search item!')
      return redirect('home')  

def contact(request):
   if request.method == 'POST':
      name = request.POST['name']      
      email_address = request.POST['email']      
      message = request.POST['message']

      Enquiry.objects.create(
         name=name,         
         email_address=email_address,
         message=message
      )
      messages.success(request, 'Your enquiry has been submitted')   
   return render(request, 'hotel_miramar/contact.html')

