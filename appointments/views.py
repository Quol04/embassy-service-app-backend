from rest_framework import generics, permissions
from .models import Appointment
from .serializers import AppointmentSerializer
from users.permissions import IsApplicant


class AppointmentCreateView(generics.CreateAPIView):
    serializer_class = AppointmentSerializer
    permission_classes = [permissions.IsAuthenticated, IsApplicant]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class MyAppointmentsListView(generics.ListAPIView):
    serializer_class = AppointmentSerializer
    permission_classes = [permissions.IsAuthenticated, IsApplicant]

    def get_queryset(self):
        return Appointment.objects.filter(user=self.request.user)
