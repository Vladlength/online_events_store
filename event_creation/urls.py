from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.main_creation, name='main_creation'),
    path('price_creation', views.create_price, name='price_creation'),

]
