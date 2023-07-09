from django.db import models
from django.core.validators import MaxLengthValidator, MinLengthValidator

# Create your models here.

class global_database(models.Model):
    name = models.CharField(max_length=50,null=False)
    phone = models.CharField(
        validators = [ MaxLengthValidator(10), MinLengthValidator(10)],max_length=10,null=False)
    location = models.CharField(max_length=25)
    spam = models.IntegerField(default=0)
     
    def __str__(self):
        return self.name
    
class app_database(models.Model):
    name = models.CharField(max_length=50,null=False)
    phone = models.CharField(
        validators = [ MaxLengthValidator(10), MinLengthValidator(10)],max_length=10,null=False)
    password = models.CharField(max_length=25)
    email = models.EmailField(blank=True, null=True)
    is_spam = models.BooleanField(default=False)
    
    def __str__(self) :
        return self.name
    
class contact(models.Model):
    name = models.CharField(max_length=100, null=False)
    phone = models.CharField(max_length=15, null=False)
    is_spam = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name
   
