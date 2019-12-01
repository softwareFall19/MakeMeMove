from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=150)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=150)
    home_id = models.IntegerField()
    info = models.TextField()
    user_id = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.name

class ContactRental(models.Model):
    name = models.CharField(max_length=150)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=150)
    rental_id = models.IntegerField()
    information = models.TextField()
    user_id = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.name
