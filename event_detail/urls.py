from django.urls import path, include
from . import views

urlpatterns = [
    path('<int:pk>/', views.detail, name='event_detail'),
    path('prices/', include('event_pay.urls'), name='prices'),
]
