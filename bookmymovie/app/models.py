from django.db import models
from django.core.validators import int_list_validator

# Create your models here.

class Screen(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, blank=False)

    class Meta:
        ordering = ['name']

class SeatInfo(models.Model):
    screen = models.ForeignKey(Screen, related_name='seat_info', on_delete=models.CASCADE)
    row = models.CharField(max_length=16, blank=False)
    num_seats = models.IntegerField(blank=True, default=0)
    aisle_seats = models.TextField(validators=[int_list_validator], blank=True, default='')

    class Meta:
        ordering = ['row']
