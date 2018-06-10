from django.forms import ModelForm
from .models import Client
from django import forms

class PersonForm(ModelForm):
    class Meta:
        model = Client
        fields = ['cli_name','cli_register']
        labels = {
            "cli_name": "Client",
            "cli_register": "Register",
        }