from django.urls import path
from . import views

app_name = 'cart'

urlpatterns = [
    path('charge/<int:event_id>/<int:quantity>/<int:price>/<int:price_id>/<int:flag>/', views.cart_charge, name='cart_charge'),
    path('booking/<int:event_id>/<int:quantity>/<int:price>/<int:price_id>/', views.booking_cart, name='booking_cart'),
    path('add/<int:product_id>/<int:price_id>/',
         views.cart_add,
         name='cart_add'),
    path('remove/<int:product_id>/',
         views.cart_remove,
         name='cart_remove'),
    path('clear/',
         views.cart_clear,
         name='cart_clear'),
    path('', views.cart_detail, name='cart_detail'),

]
