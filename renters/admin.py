from django.contrib import admin

from .models import Rental

class AdminRental(admin.ModelAdmin):

    list_display = ('id', 'property_title', 'is_posted', 'price', 'date_posted', 'city')
    list_display_links = ('property_title', 'date_posted')
    
    list_editable = ('is_posted',)
    search_fields = ('property_title', 'address', 'city', 'price', 'state', 'zipcode', 'bathrooms', 'bedrooms')



admin.site.register(Rental, AdminRental)
