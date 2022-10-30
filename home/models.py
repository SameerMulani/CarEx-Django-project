from email.policy import default
from random import choices
from unittest.util import _MAX_LENGTH
from django.db import models

#BRANDS:
class Brands(models.Model):
    name = models.CharField(max_length=50,null=False)
    description = models.CharField(max_length=100,null=False)
    origin = models.CharField(max_length=50,null=False)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = 'Brands'

#CARS:
class Cars(models.Model):
    TransChoices = [('Manual','Manual'),
    ('Automatic','Automatic'),]
    FuelType = [('Petrol','Petrol'),
    ('Diesel','Diesel'),
    ('Hybrid','Hybrid'),
    ('Electric','Electric'),

    ]
    SegmentType = [('Sedan','Sedan'),('SUV','SUV'),('Hatchback','Hatchback'),('MPV','MPV')]

    brand = models.ForeignKey(Brands,on_delete=models.CASCADE,null=True)
    segement = models.CharField(choices=SegmentType,max_length=20,null=False,default='Sedan')
    name = models.CharField(max_length=50,null=False)
    price = models.CharField(max_length=10,null=False)
    year =  models.IntegerField(null=False)
    engine = models.FloatField(null=False)
    transmission = models.CharField(choices = TransChoices,max_length=20,null=False)
    mileage = models.FloatField(max_length=10,null=False)
    fueltype = models.CharField(choices=FuelType,max_length=20,null=False)
    fueltank = models.FloatField(max_length=10,null=False)
    length = models.IntegerField(null=False)
    width = models.IntegerField(null=False)

    def __str__(self):
        return self.name 
    class Meta:
        verbose_name_plural = 'Cars'


class Profile(models.Model):

    name = models.CharField(max_length=50,null=False)
    email = models.CharField(max_length=50,null=True)
    phone = models.CharField(max_length=50,null=True)
    password = models.CharField(max_length=50,null=False)

    def __str__(self):
        return self.name + ' '+self.email + ' '+self.phone

    class Meta:
        verbose_name_plural = 'Profile'



class Review(models.Model):

    name = models.CharField(max_length=50,null=False)
    description = models.CharField(max_length=50,null=False)
    rating = models.IntegerField(null=False)
    created_at = models.DateTimeField(auto_now_add=True,null=False)
    def __str__(self):
        return self.name

    class Meta:

        verbose_name_plural = 'Review'



class CarSearchHistory(models.Model):
    brandName = models.ForeignKey(Brands,on_delete=models.CASCADE)
    carName = models.ForeignKey(Cars,on_delete=models.CASCADE)
    timeSearch = models.DateTimeField(auto_now_add=True)