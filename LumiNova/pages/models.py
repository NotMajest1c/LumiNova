

from django import forms

from django.db import models
from django.dispatch import receiver

from LumiNova.settings import STATIC_ROOT, STATICFILES_STORAGE
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# Create your models here.



class product(models.Model):
    title = models.CharField(max_length=80) #max_length = number of chars
    description = models.TextField(blank = True,null=True)
    price = models.DecimalField(max_digits=1000,decimal_places=2)
    
    
    
    #image = models.ImageField(upload_to = STATICFILES_STORAGE, null=True)
   
    
