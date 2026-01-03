from django.urls import path
from .views import (
    IssueDocumentView, 
    DocumentByAppointmentView,
    DocumentDetailView
    )

urlpatterns = [
    path('issue/', IssueDocumentView.as_view(), name='issue-document'),
    path('appointment/<int:id>/', DocumentByAppointmentView.as_view(), name='document-by-appointment'),
    path('<int:pk>/', DocumentDetailView.as_view(), name='document-detail'),
]
