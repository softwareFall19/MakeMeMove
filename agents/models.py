from django.db import models

# Create your models here.

class Agent(models.Model):
    name = models.CharField(max_length=150)
    picture = models.ImageField(upload_to='pictures/%Y/%m/%d/')
    information = models.TextField(blank=True)
    telephone = models.CharField(max_length=20)
    email = models.CharField(max_length=40)

    def __str__(self):
        return self.name
