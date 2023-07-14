from django.db import models
from autoslug import AutoSlugField
from django.template.defaultfilters import slugify
from multiselectfield import MultiSelectField
from account.models import User

class Enquiry(models.Model):
   name = models.CharField(max_length=100)   
   email_address = models.EmailField(max_length=255)
   message = models.TextField()
   date_posted = models.DateTimeField(auto_now_add=True)

   def __str__(self):
      return f'{self.name} on {self.date_posted}'

   class Meta:
      verbose_name_plural = 'Enquiries'

class Hotel(models.Model):
   feature_choices = (      
      ('Swimming pool', 'Swimming pool'),      
      ('Spa', 'Spa'),
      ('Kids play area', 'Kids play area'),
      ('Gym', 'Gym'),                        
      ('Dry cleaning', 'Dry cleaning'),
      ('Room service', 'Room service'),
      ('Ironing Service', 'Ironing Service'),      
      ('Doctor on Call', 'Doctor on Call'),      
      ('Cash payment', 'Cash payment'),
      ('Credit Card', 'Credit Card'),
      ('Waiting area', 'Waiting area'),
      ('Special service', 'Special service'),
      ('Wifi Access', 'Wifi Access'),
   )

   name = models.CharField(max_length=100)
   description = models.TextField()
   address = models.CharField(max_length=250)
   city = models.CharField(max_length=100)
   features = MultiSelectField(choices=feature_choices, blank=True, max_length=200)
   mobile_no = models.CharField(max_length=14)
   email = models.EmailField(max_length=50)
   slug = AutoSlugField(unique=True, populate_from='name', sep='-', null=True)
   created_at = models.DateTimeField(auto_now_add=True)

   def __str__(self):
      return f'{self.name}'
      
   def save(self, *args, **kwargs):
      self.slug = slugify(self.name)
      super().save(*args, **kwargs)

class Room(models.Model):
   room_options_choices = (      
      ('Air Conditioning', 'Air Conditioning'),      
      ('Wifi', 'Wifi'),
      ('Kitchen', 'Kitchen'),
      ('Free Newspaper', 'Free Newspaper'),                        
      ('Private Balcony', 'Private Balcony'),                        
      
   )

   name = models.CharField(max_length=100)
   description = models.TextField()   
   room_image_1 = models.ImageField(      
      upload_to="room_images",      
   )
   room_image_2 = models.ImageField(
      upload_to="room_images",
      null=True,
      blank=True
   )
   room_image_3 = models.ImageField(
      upload_to="room_images",
      null=True,
      blank=True
   )
   hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)      
   price = models.IntegerField()      
   room_options = MultiSelectField(choices=room_options_choices, blank=True, max_length=300)
   is_booked = models.BooleanField(default=False, blank=True, null=True)
   created_at = models.DateTimeField(auto_now_add=True)
   updated_at = models.DateTimeField(auto_now=True)
   slug = AutoSlugField(unique=True, populate_from='name', sep='-', null=True)

   def __str__(self):
      return f'{self.name} at {self.hotel.name}'
      
   def save(self, *args, **kwargs):
      self.slug = slugify(self.name)
      super().save(*args, **kwargs)

class Booking(models.Model):
   user = models.ForeignKey(User, on_delete=models.CASCADE)
   room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name="bookings")
   start_date = models.DateTimeField()
   end_date = models.DateTimeField()
   no_of_adults = models.IntegerField()
   no_of_children = models.IntegerField(blank=True, null=True)
   is_active = models.BooleanField(default=False, blank=True)   
   is_confirmed = models.BooleanField(default=False, blank=True)   
   is_cancelled = models.BooleanField(default=False, blank=True)
   is_completed = models.BooleanField(default=False, blank=True)
   booking_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)

   def __str__(self):
      return f'{self.user.username} on {self.room.name}'
   
class Feedback(models.Model):
   user = models.ForeignKey(User, on_delete=models.CASCADE)
   room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name="feedbacks")
   message = models.TextField()
   created_date = models.DateTimeField(auto_now_add=True)   

   def __str__(self):
      return f'{self.user.username} on {self.room.name}'