from django.db import models

# TODO: опишите модели датчика (Sensor) и измерения (Measurement)


class Sensor(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.description


class Measurement(models.Model):
    temperature = models.DecimalField(decimal_places=1, max_digits=4)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    sensor = models.ForeignKey('Sensor', on_delete=models.CASCADE, related_name='measurements')
    photo = models.ImageField(upload_to='images/', default=None)
