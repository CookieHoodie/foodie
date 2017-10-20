from django import forms
from django.forms import ModelForm
from .models import *

class OwnerForm(ModelForm):
    class Meta:
        model = Owner
        fields = ['name', 'date_of_birth', 'gender', 'nric', 'hp_no', 'contact_no', 'email', 'password']


class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = []