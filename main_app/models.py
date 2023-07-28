from django.db import models
from django.urls import reverse

# Create your models here.

ISLANDS = (
    ('1', 'Baltra'),
    ('2', 'Bartolomé'),
    ('3', 'Darwin'),
    ('4', 'Hood'),
    ('5', 'Fernandina'),
    ('6', 'Floreana'),
    ('7', 'Genovesa'),
    ('8', 'Isabela'),
    ('9', 'Marchena'),
    ('10', 'North Seymour'),
    ('11', 'Pinzón'),
    ('12', 'Pinta'),
    ('13', 'Rábida'),
    ('14', 'San Cristóbal'),
    ('15', 'Santa Cruz'),
    ('16', 'Santa Fe'),
    ('17', 'Santiago'),
    ('18', 'Wolf'),
)


class Finch(models.Model):
    common_name = models.CharField(max_length=100, default='')
    scientific_name = models.CharField(max_length=100, default='')
    beak_type = models.CharField(max_length=100, default='')
    image = models.CharField(max_length=500, default='')
    food = models.ManyToManyField('Food', blank=True)

    def __str__(self):
        return self.common_name
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'finch_id': self.id})

class Sighting(models.Model):
    date = models.DateField('sighting date')
    location = models.CharField(
        max_length=2,
        choices=ISLANDS,
        default=ISLANDS[0][0]
        )
    finch = models.ForeignKey(Finch, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.get_location_display()} on {self.date}"
    
    class Meta:
        ordering = ['-date']

class Food(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('foods_detail', kwargs={'pk': self.id})