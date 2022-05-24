from datetime import datetime,date
from django.db import models
from django.forms import DateTimeField

# Create your models here.
class Topic(models.Model):
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def str(self):
        return self.text

class Order(models.Model):
    name = models.CharField(max_length=50)
    full_text = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name