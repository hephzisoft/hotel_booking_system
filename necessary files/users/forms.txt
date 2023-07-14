from typing import Any
from django import forms
from account.models import User

class EditProfileForm(forms.ModelForm):
   
   username = forms.CharField(
      label='',
      widget=forms.TextInput(
         attrs={
            'placeholder': '',
            'class': 'form-control text-md bg-white',
         }
      )
   )

   first_name = forms.CharField(
      label='',
      widget=forms.TextInput(
         attrs={
            'placeholder': '',
            'class': 'form-control text-md bg-white',
         }
      )
   )

   last_name = forms.CharField(
      label='',
      widget=forms.TextInput(
         attrs={
            'placeholder': '',
            'class': 'form-control text-md bg-white',
         }
      )
   )

   profile_picture = forms.ImageField(
      label='',
      required=False,
      widget=forms.FileInput(
         attrs={
            # 'placeholder': '',
            # 'class': 'form-control text-md bg-white',
            "type": "file",
            "placeholder": "",
            "accept": "image/*",
            "class": "d-none",
            "id": "profile_picture",
            "onchange":"loadFile(event)"
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

   bio = forms.CharField(
      label='',
      required=False,
      widget=forms.Textarea(
         attrs={
            "placeholder": "",
            'class': 'form-control text-md bg-white',       
            "style": "height: 140px;resize: none;",
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

   date_of_birth = forms.DateField(
      label="",
      required=False,
      widget=forms.DateInput(
         attrs={
            "type":"date",
            'placeholder': '',
            'class': 'form-control text-md bg-white profileDate',
         }
      )
   )

   gender_choices =  [
      ('Male', 'Male'),
      ('Female', 'Female'),
      ('Other', 'Other'),      
   ]

   gender = forms.CharField(
      label='',
      required=False,      
      widget=forms.RadioSelect(
         choices=gender_choices,
         attrs={
            'class': 'd-flex gap-3 font-inter',
            'id': 'gender'
         }
      )
   )

   
   class Meta:
      model = User
      fields = (
         'username',
         'first_name',
         'last_name',
         'profile_picture',
         'email',
         'bio',
         'mobile_no',
         'city' ,
         'address',
         "date_of_birth",
         "gender", 
      )      
   
   def __init__(self, *args: Any, **kwargs: Any) -> None:
      super(EditProfileForm , self).__init__(*args, **kwargs)

      for fieldname in (
         'username',
         'first_name',
         'last_name',
         'profile_picture',
         'email',
         'bio',
         'mobile_no',
         'city' ,
         'address',
         "date_of_birth",
         "gender" 
      ):
         self.fields[fieldname].help_text = None
