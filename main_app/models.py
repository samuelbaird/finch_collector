from django.db import models

# Create your models here.

class Finch(models.Model):
    common_name = models.CharField(max_length=100, default='')
    scientific_name = models.CharField(max_length=100, default='')
    beak_type = models.CharField(max_length=100, default='')
    food = models.CharField(max_length=100, default='')
    image = models.CharField(max_length=500, default='')

    def __str__(self):
        return self.common_name