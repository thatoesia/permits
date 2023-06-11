import calendar
from select import select
from sqlite3 import Date
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import Account

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=255, help_text="email is required")
    date_of_birth = forms.DateField(widget=forms.DateInput(attrs={"placeholder": "year of birth", "type": "date"}))
    class Meta:
        model = Account
        fields = ['email', 'first_name', 'last_name', 'id_number','user_type', 'phone_number', 'date_of_birth', 
                  'gender','image', 'password1', 'password2']

class UpdateUserForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ['first_name', 'last_name','phone_number','user_type','date_of_birth', 'gender','id_number']