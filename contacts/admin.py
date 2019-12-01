from django.contrib import admin

from .models import Contact, ContactRental
class AdminContact(admin.ModelAdmin):
    list_display = ('id', 'name', 'email')
    search_fields = ('name', 'email')


admin.site.register(Contact, AdminContact)



class AdminContactRental(admin.ModelAdmin):
    list_display = ('id', 'name', 'email')
    search_fields = ('name', 'email')


admin.site.register(ContactRental, AdminContactRental)
