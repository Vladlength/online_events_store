from django.db import models
from django.contrib.auth.models import User


# for purchase
class Purchase(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event_name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.FileField(upload_to='img/')
    quantity = models.IntegerField(default=0)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user


# for booking
class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event_name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.FileField(upload_to='img/')
    quantity = models.IntegerField(default=0)
    created_on = models.DateTimeField(auto_now_add=True)
    event_id = models.IntegerField()
    price_id = models.IntegerField()
