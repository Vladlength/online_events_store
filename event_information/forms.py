from django import forms


# event search form
class Search(forms.Form):
    query = forms.CharField(label='Search', max_length=30)
