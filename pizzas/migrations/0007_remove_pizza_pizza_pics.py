# Generated by Django 3.0.5 on 2022-05-07 02:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pizzas', '0006_pizza_pizza_pics'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pizza',
            name='pizza_pics',
        ),
    ]
