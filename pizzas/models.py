from cgitb import text
from django.db import models
from this import d
from audioop import maxpp
from django.contrib.auth.models import User

# Create your models here.
class Pizza(models.Model):
    pizza_name = models.CharField(max_length=200)

    def __str__(self):
        return self.pizza_name


class Topping(models.Model):
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    topping_name = models.CharField(max_length=200)

    def __str__(self):
        return self.topping_name

class Comments(models.Model):
    comment = models.CharField(max_length=250)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.comment
