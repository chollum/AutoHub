from django.db import models

# Create your models here.

class Room(models.Model):
    tag = models.CharField(max_length=25, default='')
    description = models.CharField(max_length=100, default='Generic room')
    temperature = models.CharField(max_length=5, default=0)
    humidity = models.CharField(max_length=5, default = 0)

    def _str_(self):
        return self.name

    class Meta:
        verbose_name_plural = 'rooms'
