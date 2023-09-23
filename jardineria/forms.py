from . import models
from django.forms import ModelForm, DateInput, TimeInput

class AppointmentForm(ModelForm):
    class Meta:
        model = models.Appointment
        fields = ['client', 'contact_phone']
        labels = {
            'client': 'Ingrese su nombre',
            'contact_phone': 'Ingrese su número de contacto',
        }