from django import forms
from django.db import models

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column


from .models import Home

class SellerForm(forms.ModelForm):


    class Meta:
        model = Home
        fields = ('property_title', 'address', 'city', 'state', 'zipcode', 'information', 'price', 
                  'bedrooms', 'bathrooms', 'garage', 'homesize', 'landsize', 'top_photo', 'picture1',
                  'picture2', 'picture3', 'picture4', 'picture5', 'picture6', 'is_posted', 'date_posted'
                )

    def clean_property_title(self, *args, **kwargs):
        property_title = self.cleaned_data.get('property_title')
        word_count = len(property_title)
        if word_count > 25:
            raise forms.ValidationError("This field is too long")
        if property_title == "":
            raise forms.ValidationError("Empty. Fill the field")
        
        return property_title

    def clean_address(self, *args, **kwargs):
        address = self.cleaned_data.get('address')
        word_count = len(address)
        if word_count > 25:
            raise forms.ValidationError("This field is too long")
        if not address:
            raise forms.ValidationError("Empty. Fill the field")
        
        return address

    def clean_zipcode(self, *args, **kwargs):
        zipcode = self.cleaned_data.get('zipcode')
        word_count = len(zipcode)
        if word_count != 5:
            raise forms.ValidationError("Five numeric strings are needed")
        if not zipcode:
            raise forms.ValidationError("Empty. Choose a State")
        if not zipcode.isdigit():
            raise forms.ValidationError('Phone number can only contains digits')
    
        return zipcode

    def clean_city(self, *args, **kwargs):
        city = self.cleaned_data.get('city')
        if len(city) > 25:
            raise forms.ValidationError("This field is too long")
        if not city:
            raise forms.ValidationError("Empty. Fill the field")
        
        return city
    
    def clean_price(self, *args, **kwargs):
        price = self.cleaned_data.get('price')
        word_count = len(str(price).split())
        if word_count > 9:
             raise forms.ValidationError("This field should contain a minimum of 9 integers")
        
        return price



    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'POST'
        self.helper.layout = Layout(
            'property_title',
            'address',
            Row(
                Column('city', css_class='form-group col-md-4 mb-0'),
                Column('state', css_class='form-group col-md-4 mb-0'),
                Column('zipcode', css_class='form-group col-md-4 mb-0'),
                css_class='form-row'
            ),
            'information',
            'price',
            Row(
                Column('bedrooms', css_class='form-group col-md-4 mb-0'),
                Column('bathrooms', css_class='form-group col-md-4 mb-0'),
                Column('garage', css_class='form-group col-md-4 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('homesize', css_class='form-group col-md-4 mb-0'),
                Column('landsize', css_class='form-group col-md-4 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('top_photo', css_class='form-group col-md-4 p-4'),
                Column('picture1', css_class='form-group col-md-4 p-4'),
                Column('picture2', css_class='form-group col-md-4 p-4'),
                css_class='form-row'
            ),
            Row(
                Column('picture3', css_class='form-group col-md-4 p-4'),
                Column('picture4', css_class='form-group col-md-4 p-4'),
                css_class='form-row'
            ),
            Row(
                Column('picture5', css_class='form-group col-md-4 p-4'),
                Column('picture6', css_class='form-group col-md-4 p-4'),
                css_class='form-row'
            ),
            'is_posted',
            'date_posted',
            
            Submit('submit', 'Post your house')
        )

    
    