from django import forms

from .models import Advertise


class AdvertiseForm(forms.ModelForm):
    class Meta:
        model = Advertise
        exclude = ['ad_picture', 'card_title', 'card_text'] 