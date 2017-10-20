from django.db import models

# Create your models here.
class Owner(models.Model):
    name = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=1)
    nric = models.CharField(max_length=9, primary_key=True)
    hp_no = models.CharField(max_length=8)
    contact_no = models.CharField(max_length=10)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

class Customer(models.Model):
    name = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=1)
    contact_no = models.CharField(max_length=10)
    email = models.CharField(max_length=50, primary_key=True)
    password = models.CharField(max_length=50)