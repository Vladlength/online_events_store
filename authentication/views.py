from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from .forms import AuthUserForm, RegisterUserForm
from django.contrib.auth.models import User
from django.views.generic import CreateView
from django.contrib.auth import authenticate, login


class HomeLoginView(LoginView):
    template_name = 'login_page.html'  # the template used
    form_class = AuthUserForm  # the form used
    success_url = reverse_lazy('index')  # will be redirected on success

    # the user will be redirected after a successful login
    def get_success_url(self):
        return self.success_url


class HomeRegisterView(CreateView):
    model = User  # inherited model
    template_name = 'register_page.html'  # the template used
    form_class = RegisterUserForm  # the form used
    success_url = reverse_lazy('index')  # will be redirected on success
    success_msg = 'Пользователь создан'  # success message

    # This method is called when the form associated with the view passes validation and all form data is valid.
    def form_valid(self, form):
        # the form_valid() method of the parent class is called. allows you to perform basic validation of the form
        # and get the validation result.
        form_valid = super().form_valid(form)
        # the cleared form data is obtained
        username = form.cleaned_data["username"]
        password = form.cleaned_data["password"]
        # checks whether a user with such specified data exists in the system
        aut_user = authenticate(username=username, password=password)
        # authorizes the user by associating him with the current session.
        # This allows users to remain logged in throughout the session.
        login(self.request, aut_user)
        return form_valid


# exit
class HomeLogoutView(LogoutView):
    next_page = reverse_lazy('index')  # will be redirected on success
