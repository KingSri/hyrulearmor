from django import forms
from .models import Armor, Wear

class ArmorForm(forms.ModelForm):
    # the Meta class is where we connect to a model and define
    # the fields that make up the form
    class Meta:
        model = Armor
        fields = ('name', 'function', 'description', 'ap')

class WearForm(forms.ModelForm):
  class Meta:
    model = Wear
    fields = ['date', 'time']
