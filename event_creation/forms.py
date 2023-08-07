from django import forms
from event_information import models
import datetime


# class CreatePrice(forms.Form):
#     ticket_price = forms.FloatField(default=5.0, widget=forms.TextInput(attrs={
#         'class': 'form-control',  # css style usage
#         'placeholder': 'Введите стоимость билета'
#     }))
#     why_cost_text = forms.CharField(widget=forms.TextInput(attrs={
#         'class': 'form-control',  # css style usage
#         'placeholder': 'обоснуйте цену'
#     }))


class CreateEventForm(forms.ModelForm):
    class Meta:
        model = models.Event
        fields = ['name', 'body', 'image', 'date', 'time', 'end_time', 'place', 'prices']


class CreateEventPrice(forms.ModelForm):
    class Meta:
        model = models.EventPrice
        fields = ['price', 'why_cost_text', 'tickets_quantity']
