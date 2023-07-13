from django.contrib import admin
from .models import Portfolio
# Register your models here.

class PortfolioAdmin (admin.ModelAdmin):
    list_display = ['name' , 'type', 'description']
    list_filter = ['dateCreated']
    search_fields = ['name']
admin.site.register(Portfolio , PortfolioAdmin)
