from django import forms

from .models import Advertise


class AdvertiseForm(forms.ModelForm):
    class Meta:
        model = Advertise
        fields = ('role', 'name', 'information', 'telephone', 'email')



        



        
