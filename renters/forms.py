
from django import forms
from homes.models import Appointments

class ScheduleTourForm(forms.ModelForm):
    class Meta:
        model = Appointments
        fields= '__all__'