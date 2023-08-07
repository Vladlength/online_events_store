import django.utils.timezone
from django.db import models
from django.contrib.auth.models import User


# model to create prices for events
class EventPrice(models.Model):
    price = models.DecimalField(max_digits=10, decimal_places=2,
                                verbose_name='Цена')  # used to give a user-friendly name
    why_cost_text = models.TextField()
    tickets_quantity = models.IntegerField(default=0)

    def __str__(self):
        return str(self.price)


def get_default_user():
    return User.objects.get(username='admin').id


# model to create events
class Event(models.Model):
    name = models.CharField(max_length=60)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    image = models.FileField(upload_to='img/')
    prices = models.ManyToManyField(EventPrice, blank=True)
    date = models.DateField(default=django.utils.timezone.now)
    time = models.TimeField(default=django.utils.timezone.now)  # rename start_time for clarity
    end_time = models.TimeField(default=django.utils.timezone.now)
    place = models.CharField(max_length=60, default='hy')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='post', default=get_default_user)

    def __str__(self):
        return self.name
