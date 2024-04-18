from django.contrib import admin
from main.models import Location
# Register your models here.
@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ('postcode', 'name')
