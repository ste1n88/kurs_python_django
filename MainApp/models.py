from django.db import models

# Create your models here.

#class User(models.Model):
#    name = models.


class Color(models.Model):
    name = models.CharField(max_length=64)

class Item(models.Model):
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    count = models.PositiveIntegerField()
    description = models.CharField(max_length=512, default='Описания ещё нет')
    colors = models.ManyToManyField(to=Color)

    def __repr__(self):
        return f'Item({self.name}, {self.brand}, {self.count}, {self.description}, {self.colors}, )'

class Country(models.Model):
    country = models.CharField(max_length=128)
    population = models.PositiveIntegerField()
    capital = models.CharField(max_length=128)
    language = models.CharField(max_length=128)

    def __str__(self):
        return '%s, %s, %s, %s,' % (self.country, self.population, self.capital, self.language )


