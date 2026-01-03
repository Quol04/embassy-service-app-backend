from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404

from .models import Document
from .serializers import DocumentSerializer
from .permissions import IsStaffOrAdmin
from appointments.models import Appointment
