from django.contrib import admin


from .models import Agent

# Register your models here.

class AdminAgent(admin.ModelAdmin):
    list_display = ('id', 'name', 'email')
    list_display_links = ('name',)
    search_fields = ('name',)


admin.site.register(Agent, AdminAgent)
