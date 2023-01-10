from django.db import models

# Create your models here.
class Vis(models.Model):
    heart_beat = models.FloatField(default=90.0)
    time = models.TimeField(auto_now_add=True)

    class Meta:
        ordering = ['-time']