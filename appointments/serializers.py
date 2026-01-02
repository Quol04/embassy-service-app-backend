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
