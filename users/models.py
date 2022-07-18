from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Customer(AbstractUser):
    phone_number = models.CharField(max_length=10,blank=True)
    Address = models.CharField(max_length=400,blank=True)
