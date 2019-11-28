from django import forms
from django.contrib.auth.models import User
from .models import Car
from django.contrib.admin.widgets import AdminDateWidget

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username','email','password', 'first_name', 'last_name')


class CarRent(forms.Form):
    car_mark = forms.CharField()
    car_model = forms.CharField()

    class Meta():
        model = Car
