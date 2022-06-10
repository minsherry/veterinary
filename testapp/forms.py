
from django import forms

class TestForm(forms.Form):
    food = forms.CharField(max_length = 10, label = '食物')
    drink = forms.CharField(max_length = 10, label = '飲料')