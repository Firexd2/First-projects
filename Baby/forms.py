from django import forms
from .models import *
from datetime import datetime

class EatForm(forms.ModelForm):
    time = forms.CharField(widget=forms.TextInput(attrs={'class': "form-control", 'placeholder':"Время", 'size': '4'}))
    volume = forms.IntegerField(widget=forms.TextInput(attrs={'class': "form-control", 'placeholder':"Объем", 'size': '4'}))
    data = forms.CharField(widget=forms.TextInput(attrs={'type': 'hidden', 'value': str(datetime.today())[:10]}))

    class Meta:
        model = BabyEat
        exclude =['']


class WeightForm(forms.ModelForm):
    week = forms.IntegerField(widget=forms.TextInput(attrs={'class': "form-control", 'placeholder':"Неделя", 'size': '4'}))
    lenght = forms.IntegerField(widget=forms.TextInput(attrs={'class': "form-control", 'placeholder':"Рост", 'size': '4'}))
    weight = forms.IntegerField(widget=forms.TextInput(attrs={'class': "form-control", 'placeholder':"Вес", 'size': '4' }))

    class Meta:
        model = BabyWeight
        exclude =['']