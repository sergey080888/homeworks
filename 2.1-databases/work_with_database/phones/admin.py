from django.contrib import admin
from .models import Phone


@admin.register(Phone)
class PhoneAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'price', 'release_date', 'lte_exists',]
    list_filter = ['id', 'name', 'price', 'release_date', 'lte_exists',]
