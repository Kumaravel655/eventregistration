from django.db import models

# Create your models here.
from django.contrib import admin
class participatent(models.Model):
    username = models.CharField(max_length=100)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    insitution = models.CharField(max_length=50)
    
    
class participatentAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'phone','insitution') 


    