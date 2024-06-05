from django.db import models

# Create your models here.

#class User(models.Model):
#    name = models.


class Item(models.Model):
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    count = models.PositiveIntegerField()
    description = models.CharField(max_length=512, default='Описания ещё нет')

    def __repr__(self):
        return f'Item({self.name}, {self.brand}, {self.count}, {self.description})'
