from rest_framework import generics , status 
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken   
from .serializers import RegisterSerializer, UserSerializer, LoginSerializer
from .models import User

# Create your views here.
class RegisterViewSet(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer