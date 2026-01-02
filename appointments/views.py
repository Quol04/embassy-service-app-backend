from rest_framework import generics, permissions, filters
from .models import Appointment
from .serializers import (AppointmentSerializer,
                          AppointmentStatusUpdateSerializer,
                          AppointmentRescheduleSerializer
                          )
from users.permissions import IsApplicant, IsAdmin,IsStaff


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

class AppointmentListView(generics.ListAPIView):
    """
    Staff/Admin: View all appointments
    """
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
    permission_classes = [permissions.IsAuthenticated, IsStaff | IsAdmin]

    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['user__email', 'service__name', 'status']
    ordering_fields = ['appointment_date', 'created_at']


class AppointmentStatusUpdateView(generics.UpdateAPIView):
    """
    Staff/Admin: Approve / Reject / Complete
    """
    queryset = Appointment.objects.all()
    serializer_class = AppointmentStatusUpdateSerializer
    permission_classes = [permissions.IsAuthenticated, IsStaff | IsAdmin]


class AppointmentRescheduleView(generics.UpdateAPIView):
    """
    Staff/Admin: Reschedule appointment
    """
    queryset = Appointment.objects.all()
    serializer_class = AppointmentRescheduleSerializer
    permission_classes = [permissions.IsAuthenticated, IsStaff | IsAdmin]