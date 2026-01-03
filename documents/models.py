from django.db import models
from django.conf import settings
from appointments.models import Appointment

# Create your models here.

User = settings.AUTH_USER_MODEL

class Document(models.Model):
    DOCUMENT_TYPES = (
        ('passport','Passport'),
        ('id','ID'),
        ('certificate', 'Certificate'),
        ('permit', 'Permit'),
        ('license', 'License'),
        
    )
    appointment = models.OneToOneField(
        Appointment,
        on_delete=models.CASCADE,
        related_name='document'
    )
    issued_to = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='documents'
    )
    document_type = models.CharField(max_length=50, choices=DOCUMENT_TYPES)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True) 
    content = models.TextField()
    issued_at = models.DateTimeField(auto_now_add=True)
    issued_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        related_name='issued_documents'
    )

    def __str__(self):
        return f"{self.title} - {self.issued_to}"



