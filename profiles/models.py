from django.db import models
from django.contrib.auth.models import User


class Address(models.Model):
    street = models.CharField(max_length=50)
    house_number = models.CharField(max_length=10)
    postal_code = models.CharField(max_length=10)
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=50)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    calling_name = models.CharField(max_length=20)
    birthdate = models.DateField()
    address = models.OneToOneField(Address, on_delete=models.CASCADE)

