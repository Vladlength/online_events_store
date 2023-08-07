from django import forms

EVENT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 21)]


# form for adding an item to the cart
class CartAddProductForm(forms.Form):
    quantity = forms.TypedChoiceField(coerce=int, choices=EVENT_QUANTITY_CHOICES, label="Количество")
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)
