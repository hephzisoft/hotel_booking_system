from django import forms
from hotel_miramar.models import Booking, Room, Hotel, Feedback


class AddRoomForm(forms.ModelForm):
   name = forms.CharField(
      label='',
      widget=forms.TextInput(
         attrs={
            'placeholder': '',
            'class': 'form-control text-md bg-white mb-3',
         }
      )
   )

   description = forms.CharField(
      label='',      
      widget=forms.Textarea(
         attrs={
            "placeholder": "",
            'class': 'form-control text-md bg-white mb-3',       
            "style": "height: 140px;resize: none;",
         }
      )
   )   

   room_image_1 = forms.ImageField(
      label='',
      widget=forms.FileInput(
         attrs={
            "type": "file",
            "placeholder": "",
            "class": "form-control text-sm font-medium mb-3",
         }
      )
   )

   room_image_2 = forms.ImageField(
      label='',
      required=False,
      widget=forms.FileInput(
         attrs={
            "type": "file",
            "placeholder": "",
            "class": "form-control text-sm font-medium mb-3",
         }
      )
   )

   room_image_3 = forms.ImageField(
      label='',
      required=False,
      widget=forms.FileInput(
         attrs={
            "type": "file",
            "placeholder": "",
            "class": "form-control text-sm font-medium mb-3",
         }
      )
   )

   hotel = forms.ModelChoiceField(
      label='',
      queryset=Hotel.objects.all(),
      widget=forms.Select(         
         attrs={
            'placeholder': '',
            'class': 'form-control text-md font-medium mb-3',            
         }
      )
   )

   price = forms.IntegerField(
      label='',
      widget=forms.NumberInput(
         attrs={
            'placeholder': '0',
            'min': "0",
            'class': 'form-control font-medium text-md bg-white',
         }
      )
   )
   
   class Meta:
      model = Room
      fields = (
         'name', 
         'description', 
         'room_image_1',
         'room_image_2',
         'room_image_3',
         'hotel',
         'price',
         'room_options',         
      )

class EditRoomForm(forms.ModelForm):
   name = forms.CharField(
      label='',
      widget=forms.TextInput(
         attrs={
            'placeholder': '',
            'class': 'form-control text-md bg-white mb-3',
         }
      )
   )

   description = forms.CharField(
      label='',      
      widget=forms.Textarea(
         attrs={
            "placeholder": "",
            'class': 'form-control text-md bg-white mb-3',       
            "style": "height: 140px;resize: none;",
         }
      )
   )   

   room_image_1 = forms.ImageField(
      label='',
      widget=forms.FileInput(
         attrs={
            "type": "file",
            "placeholder": "",
            "class": "form-control text-sm font-medium mb-3",
         }
      )
   )

   room_image_2 = forms.ImageField(
      label='',
      required=False,
      widget=forms.FileInput(
         attrs={
            "type": "file",
            "placeholder": "",
            "class": "form-control text-sm font-medium mb-3",
         }
      )
   )

   room_image_3 = forms.ImageField(
      label='',
      required=False,
      widget=forms.FileInput(
         attrs={
            "type": "file",
            "placeholder": "",
            "class": "form-control text-sm font-medium mb-3",
         }
      )
   )

   hotel = forms.ModelChoiceField(
      label='',
      queryset=Hotel.objects.all(),
      widget=forms.Select(         
         attrs={
            'placeholder': '',
            'class': 'form-control text-md font-medium mb-3',            
         }
      )
   )

   price = forms.IntegerField(
      label='',
      widget=forms.NumberInput(
         attrs={
            'placeholder': '0',
            'min': "0",
            'class': 'form-control font-medium text-md bg-white',
         }
      )
   )

   is_booked = forms.BooleanField(
      label='',
      required=False,
      widget=forms.CheckboxInput(
         attrs={
            'class': 'font-semibold text-md',
         }
      )
   )
   
   class Meta:
      model = Room
      fields = (
         'name', 
         'description', 
         'room_image_1',
         'room_image_2',
         'room_image_3',
         'hotel',
         'price',
         'room_options', 
         'is_booked'        
      )

class AddHotelForm(forms.ModelForm):
   name = forms.CharField(
      label='',
      widget=forms.TextInput(
         attrs={
            'placeholder': '',
            'class': 'form-control text-md bg-white mb-3',
         }
      )
   )

   description = forms.CharField(
      label='',      
      widget=forms.Textarea(
         attrs={
            "placeholder": "",
            'class': 'form-control text-md bg-white mb-3',       
            "style": "height: 140px;resize: none;",
         }
      )
   )   

   address = forms.CharField(
      label='',
      required=False,
      widget=forms.TextInput(
         attrs={
            'placeholder': '',
            'class': 'form-control text-md bg-white',
         }
      )
   )

   city = forms.CharField(
      label='',
      required=False,
      widget=forms.TextInput(
         attrs={
            'placeholder': '',
            'class': 'form-control text-md bg-white',
         }
      )
   )

   mobile_no = forms.CharField(
      label='',
      max_length=14,
      required=False,
      widget=forms.TextInput(
         attrs={
            'placeholder': '',
            'class': 'form-control text-md bg-white',
         }
      )
   )

   email = forms.EmailField(
      label='Email',
      widget=forms.EmailInput(
         attrs={
            'placeholder': '',
            'class': 'form-control text-md bg-white'
         }
      ),
   )

   class Meta:
      model = Hotel
      fields = ('name', 'description', 'address', 'city', 'features', 'mobile_no', 'email')

class BookingForm(forms.ModelForm):
   no_of_adults = forms.IntegerField(
      label='',
      widget=forms.NumberInput(
         attrs={
            'placeholder': '0',
            'min': "0",
            'class': 'form-control font-medium text-md bg-white',
         }
      )
   )

   no_of_children = forms.IntegerField(
      label='',
      required=False,
      widget=forms.NumberInput(
         attrs={
            'placeholder': '0',
            'min': "0",
            'class': 'form-control font-medium text-md bg-white',
         }
      )
   )

   start_date = forms.DateTimeField(
      label='',
      widget=forms.DateInput(
         attrs={
            'type': 'datetime-local',
            'placeholder': '',
            'class': 'form-control font-medium text-md bg-white',
         }
      )
   )

   end_date = forms.DateTimeField(
      label='',
      widget=forms.DateInput(
         attrs={
            'type': 'datetime-local',
            'placeholder': '',
            'class': 'form-control font-medium text-md bg-white',
         }
      )
   )

   class Meta:
      model = Booking
      fields = ('no_of_adults', 'no_of_children', 'start_date', 'end_date')   
      
class FeedBackForm(forms.ModelForm):
   message = forms.CharField(
      label='',      
      widget=forms.Textarea(
         attrs={
            "placeholder": "",
            'class': 'form-control text-md bg-white mb-3',       
            "style": "height: 100px;resize: none;",
         }
      )
   )  
   
   class Meta:
      model = Feedback
      fields = ('message',)