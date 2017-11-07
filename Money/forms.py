from django import forms
from .models import *

class MoneyForm(forms.ModelForm):
    amount = forms.IntegerField(widget=forms.TextInput(attrs={'class': "form-control", 'size': '4'}))

    class Meta:
        model = monthMoney
        exclude = ["one", "two", "three", "four", "five", "date"]

class CostForm(forms.ModelForm):

    one_cost = forms.IntegerField(widget=forms.TextInput(attrs={'class': "form-control", 'id': 'cost0', 'size': '2', 'value': '0'}))
    two_cost = forms.IntegerField(widget=forms.TextInput(attrs={'class': "form-control", 'id': 'cost1', 'size': '2', 'value': '0'}))
    three_cost = forms.IntegerField(widget=forms.TextInput(attrs={'class': "form-control", 'id': 'cost2', 'size': '2', 'value': '0'}))
    four_cost = forms.IntegerField(widget=forms.TextInput(attrs={'class': "form-control", 'id': 'cost3', 'size': '2', 'value': '0'}))
    five_cost = forms.IntegerField(widget=forms.TextInput(attrs={'class': "form-control", 'id': 'cost4', 'size': '2', 'value': '0'}))

    class Meta:
        model = Costs
        exclude = ['amount_cost']

class BankForm(forms.ModelForm):
    bank = forms.IntegerField(widget=forms.TextInput(attrs={'class': "form-control", 'size': '4'}))

    class Meta:
        model = Bank
        exclude = [""]

class ActionForm(forms.ModelForm):
    text = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'size': '4'}))

    class Meta:
        model = LastAction
        exclude = ['date']