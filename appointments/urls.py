from django.urls import path
from .views import AppointmentCreateView, MyAppointmentsListView

urlpatterns=[
    
    path('appointments/', AppointmentCreateView.as_view(), name='appointment-create'),
    path('appointment/my/', MyAppointmentsListView.as_view(), name='my-appointments')
]
