from dataclasses import field, fields
from django.forms import ModelForm
from mysite.models import User
from mysite.models import Advert
from django import forms


class UserForm(ModelForm):
    class Meta:
        model= User 
        fields= '__all__'
        
        
    
    
class AdvertForm(ModelForm):
    class Meta:
        model= Advert
        fields= '__all__'
        