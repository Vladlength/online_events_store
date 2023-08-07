from django.contrib import admin
from .models import Event
# register the purchase model to see it in the admin panel

admin.site.register(Event)


