import email
from this import d
from turtle import position
from django.db import models

# Create your models here.

class User(models.Model):
    first_name= models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    phone_number = models.CharField(max_length=12)
    department = models.CharField(max_length=100)
    date_of_birth = models.CharField(max_length=20)
  

    class Meta: 
        ordering = ['first_name', 'last_name', 'email', 'phone_number','department','date_of_birth']
        
        def __str__(self):
                return f"{self.first_name} "
    

class Advert (models.Model):
    company = models.CharField(max_length=200 )
    position = models.CharField(max_length=200)
    explanation= models.CharField(max_length=400)
    category = models.CharField(max_length=200)
    users= models.ManyToManyField(User)
    
    class Meta: 
        ordering= ['company','position','explanation', 'category']
    
        def __str__(self) :
            return  f"{self.company} "
    
    
class Company (models.Model):
    name = models.CharField(max_length=200)
    email =models.EmailField(max_length=200)
    phone_number = models.CharField(max_length=12)
    address = models.CharField(max_length=1024)
    category = models.CharField(max_length=200)
    
    
    
        
class AdvertUser (models.Model):
    advert_id=models.ForeignKey(Advert,on_delete=models.CASCADE)
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    
            
