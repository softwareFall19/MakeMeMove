from django.db import models

class Advertise(models.Model):
    Role_Choices = (
        ("An agent/broker", "An agent/broker"), ("Homebuyer/seller", "Homebuyer/seller"), ("Other professionals", "Other professionals"),

    )
    role = models.CharField(max_length=100, choices= Role_Choices)
    name = models.CharField(max_length=150)
    information = models.TextField(blank=True)
    telephone = models.CharField(max_length=20)
    email = models.EmailField(max_length=40)
    ad_picture = models.ImageField(upload_to='pictures/%Y/%m/%d/')
    card_title = models.CharField(max_length=100, default='')
    card_text = models.CharField(max_length=200, default='')

    def __str__(self):
        return self.name

