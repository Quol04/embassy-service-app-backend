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
    path('', AppointmentCreateView.as_view(), name='appointment-create'),
    path('my/', MyAppointmentsListView.as_view(), name='my-appointments'),

    # staff/admin routes
    path('all/', AppointmentListView.as_view()),
    path('<int:pk>/status/', AppointmentStatusUpdateView.as_view()),
    path('<int:pk>/reschedule/', AppointmentRescheduleView.as_view()),

]
