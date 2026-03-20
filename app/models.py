from django.db import models

# Create your models here.

class WeatherRecord(models.Model):
    city = models.CharField(max_length=100)
    temperature = models.FloatField()
    description = models.CharField(max_length=200)
    icon = models.CharField(max_length=10)
    emoji = models.CharField(max_length=10, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.city} - {self.temperature}°C"
