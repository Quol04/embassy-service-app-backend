from django.urls import path
from .views import (
    AppointmentCreateView, 
    MyAppointmentsListView,
    AppointmentListView,
    AppointmentStatusUpdateView,
    AppointmentRescheduleView,
    )

urlpatterns=[
    # appicant routes
    path('appointments/', AppointmentCreateView.as_view(), name='appointment-create'),
    path('appointment/my/', MyAppointmentsListView.as_view(), name='my-appointments'),

    # staff/admin routes
    path('appointments/all/', AppointmentListView.as_view()),
    path('appointments/<int:pk>/status/', AppointmentStatusUpdateView.as_view()),
    path('appointments/<int:pk>/reschedule/', AppointmentRescheduleView.as_view()),

]
