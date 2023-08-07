
from django.urls import path
from . import views

urlpatterns = [

    path('', views.user_inf, name='user_page'),

]