from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Buyer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

class Seller(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

class Renter(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)