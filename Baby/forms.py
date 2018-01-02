from django import forms
from .models import *
from django.forms.widgets import *
from datetime import datetime

class EatForm(forms.ModelForm):

    data = forms.CharField(widget=forms.TextInput(attrs={'type': 'hidden', 'value': str(datetime.today())[:10]}))

    class Meta:
        model = BabyEat
        exclude =['']
        widgets = {
            'time': TextInput(attrs={'class': "form-control", 'placeholder':'00:00', 'size': '4'}),
            'volume_mixture': TextInput(attrs={'class': "form-control", 'size': '4'}),
            'volume_porridge': TextInput(attrs={'class': "form-control", 'size': '4'}),
            'volume_puree': TextInput(attrs={'class': "form-control", 'size': '4'})
        }

class WeightForm(forms.ModelForm):
    week = forms.IntegerField(widget=forms.TextInput(attrs={'class': "form-control", 'placeholder':"Неделя", 'size': '4'}))
    lenght = forms.IntegerField(widget=forms.TextInput(attrs={'class': "form-control", 'placeholder':"Рост", 'size': '4'}))
    weight = forms.IntegerField(widget=forms.TextInput(attrs={'class': "form-control", 'placeholder':"Вес", 'size': '4' }))

    class Meta:
        model = BabyWeight
        exclude =['']