from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404

from .models import Document
from .serializers import DocumentSerializer
from .permissions import IsStaffOrAdmin
from appointments.models import Appointment

from rest_framework.generics import RetrieveUpdateDestroyAPIView


class IssueDocumentView(APIView):
    permission_classes = [IsAuthenticated, IsStaffOrAdmin]

    def post(self, request):
        appointment_id = request.data.get('appointment')

        appointment = get_object_or_404(Appointment, id=appointment_id)

        if hasattr(appointment, 'document'):
            return Response(
                {"detail": "Document already issued for this appointment."},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = DocumentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(
                issued_to=appointment.user,
                issued_by=request.user,
                appointment=appointment
            )
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DocumentByAppointmentView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, id):
        document = get_object_or_404(Document, appointment_id=id)

        # Applicant can only view their own document
        if request.user != document.issued_to and not request.user.is_staff:
            return Response(
                {"detail": "Not authorized."},
                status=status.HTTP_403_FORBIDDEN
            )

        serializer = DocumentSerializer(document)
        return Response(serializer.data)

class DocumentDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer
    permission_classes = [IsAuthenticated, IsStaffOrAdmin]
