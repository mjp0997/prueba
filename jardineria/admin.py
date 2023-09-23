from django.contrib import admin
from .models import Appointment, Gardener

# Register your models here.

admin.site.register(Gardener)
admin.site.register(Appointment)