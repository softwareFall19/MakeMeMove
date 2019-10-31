from django.contrib import admin

from .models import Home

# Register your models here.

class AdminHome(admin.ModelAdmin):

    list_display = ('id', 'property_title', 'is_posted', 'price', 'date_posted', 'city', 'agent')
    list_display_links = ('property_title', 'date_posted')
    list_filter = ('agent', 'city')
    list_editable = ('is_posted',)
    search_fields = ('property_title', 'address', 'city', 'price', 'state', 'zipcode', 'bathrooms', 'bedrooms')

admin.site.register(Home, AdminHome)