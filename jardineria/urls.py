from django.urls import path
from . import views

app_name = 'appointments'

urlpatterns = [
    path('', views.index, name='index'),
    path('crear', views.create, name='create'),
    path('<int:appointment_id>', views.detail, name='detail'),
    path('schedule/<int:appointment_id>', views.schedule, name='schedule'),
    path('finish/<int:appointment_id>', views.finish, name='finish'),
]
