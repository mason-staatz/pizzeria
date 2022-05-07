from cgitb import text
from django.db import models
from this import d
from audioop import maxpp
from django.contrib.auth.models import User
from pizzeria.settings import MEDIA_URL


# Create your models here.
class Pizza(models.Model):
    pizza_name = models.CharField(max_length=200)
    pizza_pics = models.ImageField(upload_to='img', blank= True, null= True)

    def __str__(self):
        return self.pizza_name


class Topping(models.Model):
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    topping_name = models.CharField(max_length=200)

    def __str__(self):
        return self.topping_name

class Comments(models.Model):
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    comment = models.CharField(max_length=250)
    
    def __str__(self):
        return self.comment
