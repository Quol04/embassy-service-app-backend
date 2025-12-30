from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Service
from .serializers import ServiceSerializer
from users.permissions import IsAdmin,IsStaff

# Create your views here.
class ServiceViewSet(ModelViewSet):
    queryset= Service.objects.filter(is_active= True)
    serializer_class= ServiceSerializer


    def get_permissions(self):
        if self.action in ['list','retrieve']:
            return [AllowAny()]
        elif self.action in ['create','update','partial_update']:
            return [IsAuthenticated(),IsStaff()]
        elif self.action=='destroy':
            return [IsAuthenticated(),IsAdmin()]
        return super().get_permissions()
