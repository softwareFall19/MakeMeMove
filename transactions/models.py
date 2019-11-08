from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.


class Buyer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

class Seller(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    property_title = models.CharField(max_length=150)
    address = models.CharField(max_length=150)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=100)
    information = models.TextField(blank=True)
    price = models.IntegerField()
    bedrooms = models.IntegerField()
    bathrooms = models.DecimalField(max_digits=2, decimal_places=1)
    garage = models.IntegerField(default=0)
    homesize = models.IntegerField()
    landsize = models.DecimalField(max_digits=5, decimal_places=1)
    top_photo = models.ImageField(upload_to='pictures/%Y/%m/%d/')
    picture1 = models.ImageField(upload_to='pictures/%Y/%m/%d/', blank=True)
    picture2 = models.ImageField(upload_to='pictures/%Y/%m/%d/', blank=True)
    picture3 = models.ImageField(upload_to='pictures/%Y/%m/%d/', blank=True)
    picture4 = models.ImageField(upload_to='pictures/%Y/%m/%d/', blank=True)
    picture5 = models.ImageField(upload_to='pictures/%Y/%m/%d/', blank=True)
    picture6 = models.ImageField(upload_to='pictures/%Y/%m/%d/', blank=True)
    is_posted = models.BooleanField(default=True)
    date_posted = models.DateTimeField(default=datetime.now, blank=True)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

class Renter(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)