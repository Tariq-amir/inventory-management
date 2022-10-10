from asyncio.format_helpers import extract_stack
from dataclasses import field
import email
from enum import unique
from math import fabs
from multiprocessing.sharedctypes import Value
from secrets import choice
from turtle import onclick
from django import forms
from django.contrib.auth import authenticate
from .models import Product, Search
from django.utils.safestring import mark_safe


class DateInput(forms.DateInput):
    input_type = 'date'


class ProductForm(forms.ModelForm):
    places = [('null', '---'), ('classroom', 'Class Room'), ('lab', 'Lab'),
              ('office', 'Office'), ('others', 'Others')]
    rooms = [
        ('null', '---'),
        ('101', '101'),
        ('102', '102'),
        ('103', '103'),
        ('104', '104'),
        ('201', '201'),
        ('202', '202'),
        ('203', '203'),
        ('204', '204'),
        ('ACL', 'ACL'),
        ('GD Lab', 'GD Lab'),
        ('H/W Lab', 'H/W Lab'),
        ('OS Lab', 'OS Lab'),
        ('N/W Lab', 'N/W Lab'),
        ('PG Lab', 'PG Lab'),
        ('S/W Lab', 'S/W Lab'),
        ('Faculty Office', 'Faculty Office'),
        ('Staff Office', 'Staff Office'),
        ('Seminar Room', 'Seminar Room')
    ]

    name = forms.CharField(label=mark_safe('<br>Name'))
    model = forms.CharField(label=mark_safe('<br>Model'))
    quantity = forms.IntegerField(label=mark_safe('<br>Quantity'))
    price = forms.IntegerField(label=mark_safe('<br>Price'))
    alloted = forms.ChoiceField(choices=places, label=mark_safe(
        '<br>Alloted'), required=True, widget=forms.Select)
    room = forms.ChoiceField(choices=rooms, required=True, widget=forms.Select)
    date_of_buy = forms.DateTimeField(
        widget=DateInput, label=mark_safe('<br>Date of buy'))

    class Meta:
        model = Product
        fields = ['tender_no', 'name', 'model',
                  'quantity', 'price', 'date_of_buy', 'alloted', 'room']


class SearchForm(forms.ModelForm):

    class Meta:
        model = Search
        fields = ['text']
        widgets = {
            'text': forms.TextInput(attrs={'placeholder': 'Tender No'}),
        }
