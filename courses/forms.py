from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
class UserSignUpForm(UserCreationForm): #in built user signup form for input validations and save the user details
   email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

   class Meta:
    model = User
    fields = ['username','email', 'password1', 'password2']