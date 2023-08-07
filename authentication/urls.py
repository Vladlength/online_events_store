from django.urls import path, include
from . import views

urlpatterns = [
    path('login', views.HomeLoginView.as_view(), name='login_page'),
    path('registration', views.HomeRegisterView.as_view(), name='register_page'),
    path('logout', views.HomeLogoutView.as_view(), name='logout_page'),  # exit

]
