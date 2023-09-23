from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.contrib import messages

from .models import Appointment, Gardener
from .forms import AppointmentForm

# Create your views here.
def index(request):
    appointments = Appointment.objects.all()

    return render(
        request,
        'index.html',
        context={'appointments': appointments}
    )

def detail(request, appointment_id):
    appointment = get_object_or_404(Appointment, id=appointment_id)

    return render(
        request,
        'detail.html',
        context={'appointment': appointment}
    )

def create(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()

            messages.success(request, 'Su cita fue registrada exitosamente')
            
            return HttpResponseRedirect('/crear')
    else:
        form = AppointmentForm()

    return render(
        request,
        'create.html',
        {'form': form}
    )

def schedule(request, appointment_id):
    appointment = get_object_or_404(Appointment, id=appointment_id)

    gardeners = Gardener.objects.all()

    if request.method == 'POST':
        print(request.POST)
        appointment.gardener = get_object_or_404(Gardener, id=request.POST.get('gardener'))
        appointment.address = request.POST.get('address')
        appointment.lon = request.POST.get('lon')
        appointment.lat = request.POST.get('lat')
        appointment.scheduled_to = request.POST.get('scheduled_to')
        appointment.scheduled_at = request.POST.get('scheduled_at')
        appointment.status = 'P'
        appointment.save()

        messages.success(request, 'La cita fue procesada exitosamente')
        
        return HttpResponseRedirect(f'/{appointment.id}')

    return render(
        request,
        'schedule.html',
        context={'appointment': appointment, 'gardeners': gardeners}
    )

def finish(request, appointment_id):
    appointment = get_object_or_404(Appointment, id=appointment_id)

    appointment.status = 'T'
    appointment.save()

    messages.success(request, 'La cita fue finalizada exitosamente')
    
    return HttpResponseRedirect(f'/{appointment.id}')