from django.db import models
from django.contrib.auth.models import AbstractUser
from autoslug import AutoSlugField
from django.db.models.signals import pre_delete
from django.dispatch.dispatcher import receiver
from django.template.defaultfilters import slugify

# Create your models here.
class User(AbstractUser):
   gender_choices = (
      ("Male", "Male"),
      ("Female", "Female"),
      ("Other", "Other"),           
   )
   email = models.EmailField(blank=False, null=False)
   profile_picture = models.ImageField(
      null=True,
      blank=True,
      upload_to="profile_images",
      max_length=500      
   )      
   bio = models.TextField(blank=True)
   city = models.CharField(max_length=100, blank=True, null=True)
   address = models.CharField(max_length=250, blank=True)
   mobile_no = models.CharField(max_length=14, blank=True)
   date_of_birth = models.DateField(null=True, blank=True)
   gender = models.CharField(max_length=50, choices=gender_choices, null=True, blank=True)   
   slug = AutoSlugField(unique=True, populate_from="username", sep="_", null=True)

   def __str__(self):
      return f"{self.username}"

   def save(self, *args, **kwargs):
      self.slug = slugify(self.username)
      super().save(*args, **kwargs)

@receiver(pre_delete, sender=User)
def user_image_delete(sender, instance, **kwargs):
   instance.file.delete(False)