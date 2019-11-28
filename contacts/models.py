from django.db import models

class Contact(models.Model):
    home = models.CharField(max_length=150)
    name = models.CharField(max_length=150)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=150)
    home_id = models.IntegerField(default=0)
    message = models.TextField(blank=True)
    user_id = models.IntegerField(default=0)

    def __str__(self):
        return self.name