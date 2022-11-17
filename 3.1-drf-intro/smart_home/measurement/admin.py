from django.contrib import admin

# Register your models here.
from .models import Sensor, Measurement


@admin.register(Sensor)
class SensorAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description']


@admin.register(Measurement)
class MeasurementAdmin(admin.ModelAdmin):
    list_display = ["id", 'temperature', 'created_at', 'updated_at', 'sensor', 'photo']
