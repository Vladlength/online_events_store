from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('search', views.project_search, name='project_search'),
    path('detail/', include('event_detail.urls'), name='event_detail'),
    path('authentification/', include('authentication.urls')),
]


