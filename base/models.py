from django.db import models

# Create your models here.
class pizza(models.Model):
    PizzaType = (
    (
        'regular','regular'
    ),
     (
        'square','square'
    ),
    )
    name= models.CharField(max_length=100)
    Type= models.CharField(max_length=100, choices=PizzaType )
    size= models.CharField(max_length=20)
    toppings = models.CharField(max_length=400)
