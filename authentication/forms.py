from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm


# Authentication form for the user
class AuthUserForm(AuthenticationForm, forms.ModelForm):
    class Meta:
        # inherit from
        model = User
        # which fields from the User model will be displayed in the registration form
        fields = ('username', 'password')

    def __init__(self, *args, **kwargs):
        # allows you to pass all passed arguments
        super().__init__(*args, **kwargs)
        # sets the CSS class `"form-control"` for widgets of all form fields
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'


# Registration form for the user
class RegisterUserForm(forms.ModelForm):
    class Meta:
        # inherit from
        model = User
        # which fields from the User model will be displayed in the registration form
        fields = ('username', 'password')

    def __init__(self, *args, **kwargs):
        # allows you to pass all passed arguments
        super().__init__(*args, **kwargs)
        # sets the CSS class `"form-control"` for widgets of all form fields
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'

    def save(self, commit=True):
        # Create new user
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            # saving the user in the database
            user.save()
            #  does the self object have a save_m2m() method
            if hasattr(self, "save_m2m"):
                self.save_m2m()
        return user
