from asyncio.windows_events import NULL
from django.db import models
from django import forms

class DateInput(forms.DateInput):
    input_type = 'date'


class Product(models.Model):
    tender_no = models.IntegerField(default=NULL)
    name = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    quantity = models.IntegerField(default=0)
    price = models.IntegerField(default=0)
    date_of_buy = models.DateTimeField()
    alloted = models.CharField(max_length=50)
    room = models.CharField(max_length=50)
    month_year=models.CharField(max_length=100)
    year=models.CharField(max_length=10,default='2022')
