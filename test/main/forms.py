from tkinter import Widget
from .models import Order
from django.forms import ModelForm, TextInput, DateTimeInput


class OrderForm(ModelForm):
    class Meta():
        model = Order
        fields = ['name', 'full_text']


        widgets = {
            'name': TextInput(attrs={
                'class':'form-control',
                'placeholder':'Name'
            }),
            'full_text': TextInput(attrs={
                'class':'form-control',
                'placeholder':'Full_text'
            })
    

        }