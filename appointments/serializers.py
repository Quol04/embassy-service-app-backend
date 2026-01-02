from rest_framework import serializers
from datetime import date
from .models import Appointment


class AppointmentSerializer(serializers.ModelSerializer):
    service_name = serializers.ReadOnlyField(source='service.name')

    class Meta:
        model = Appointment
        fields = [
            'id',
            'service',
            'service_name',
            'appointment_date',
            'appointment_time',
            'status',
            'created_at',
        ]
        read_only_fields = ['status', 'created_at']

    def validate_appointment_date(self, value):
        if value < date.today():
            raise serializers.ValidationError(
                "You cannot book an appointment in the past."
            )
        return value

    def validate(self, data):
        user = self.context['request'].user

        # Prevent multiple pending appointments for same service
        if Appointment.objects.filter(
            user=user,
            service=data['service'],
            status=Appointment.STATUS_PENDING
        ).exists():
            raise serializers.ValidationError(
                "You already have a pending appointment for this service."
            )

        return data

# Appointment management
class AppointmentStatusUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = ['status']

    def validate_status(self, value):
        instance = self.instance

        allowed_transitions = {
            Appointment.STATUS_PENDING: [
                Appointment.STATUS_APPROVED,
                Appointment.STATUS_REJECTED,
            ],
            Appointment.STATUS_APPROVED: [
                Appointment.STATUS_COMPLETED,
            ],
        }

        if instance.status not in allowed_transitions:
            raise serializers.ValidationError(
                "This appointment cannot be updated."
            )

        if value not in allowed_transitions.get(instance.status, []):
            raise serializers.ValidationError(
                f"Invalid status transition from {instance.status} to {value}"
            )

        return value


class AppointmentRescheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = ['appointment_date', 'appointment_time']

    def validate_appointment_date(self, value):
        if value < date.today():
            raise serializers.ValidationError(
                "Cannot reschedule to a past date."
            )
        return value