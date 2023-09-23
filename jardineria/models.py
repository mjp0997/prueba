from django.db import models
from django.utils import timezone
from django.core.validators import RegexValidator

# Create your models here.

class Gardener(models.Model):
    name = models.CharField(max_length=255)

class Appointment(models.Model):
    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$',
        message="El teléfono debe tener en el siguiente formato: '+999999999'. Hasta 15 caracteres."
    )
    STATUS_OPTIONS = [
        ("S", "Sin procesar"),
        ("P", "Procesada"),
        ("T", "Terminada"),
    ]

    # Attributes

    status = models.CharField(max_length=255, choices=STATUS_OPTIONS, default="S")

    client = models.CharField(max_length=255)
    contact_phone = models.CharField(validators=[phone_regex], max_length=255)

    address = models.CharField(max_length=255, null=True)
    lat = models.FloatField(null=True)
    lon = models.FloatField(null=True)

    gardener = models.ForeignKey(Gardener, null=True, on_delete=models.SET_NULL)

    scheduled_to = models.DateField(null=True)
    scheduled_at = models.TimeField(null=True)

    created_at = models.DateTimeField(default=timezone.now)

    # Methods

    @property
    def status_value(self) -> str:
        for key, value in self.STATUS_OPTIONS:
            if key == self.status:
                return value
        return ''
