from django.db import models
from django.contrib.auth.models import User
# from django.db.models.signals import post_save
# from django.dispatch import receiver

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    #birth_date = models.DateField(null=True, blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)
    email_confirmed = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

class Payment(models.Model):
    name = models.CharField(max_length=500)
    amount = models.IntegerField()

    def __str__(self):
        return self.name

# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)

# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     instance.profile.save()

