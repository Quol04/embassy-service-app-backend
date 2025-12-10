from rest_framework import generics , status , permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken  

from .serializers import RegisterSerializer, LoginSerializer, ProfileSerializer
from .models import User
from .permissions import IsAdmin

# Create your views here.
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = serializer.validated_data

        refresh = RefreshToken.for_user(user)

        return Response({
            'user': {
                'id': user.id,
                'username': user.username,
                'email': user.email,
                'role': user.role,
                'date_joined': user.date_joined,
            },
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }, status=status.HTTP_200_OK)
    

# profile view

class ProfileView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        serializer = ProfileSerializer(request.user)
        return Response(serializer.data)
    
    def patch(self, request):
        serializer = ProfileSerializer(request.user, data=request.data, partial=True)

        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)


# admin gets all users 

class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class= ProfileSerializer
    permission_classes= [IsAdmin]

# admin updates user roles 

class UserRoleUpdateView(APIView):
    permission_classes = [IsAdmin]

    def patch(self, request, user_id):
        try:
            user= User.objects.get(id =user_id)
        except User.DoesNotExist:
            return Response({'detail': 'User not found'}, status= 404)
        
        new_role = request.data.get('role')
        if new_role not in ['APPLICANT','STAFF','ADMIN']:
            return Response({'detail': 'Invalid role'}, status=400)
        
        user.role =new_role
        user.save()

        return Response({
            'message':'user role updated successfully',
            'user': ProfileSerializer(user).data
        })



# admin deletes a user 
class UserDeleteView(APIView):
    permission_classes = [IsAdmin]

    def delete(self, request, user_id):
        try:
            user= User.objects.get(id = user_id)

        except User.DoesNotExist:
            return Response({'detail':'User does not exist'},status=404)
        
        user.delete()
        return Response({'message':'User deleted successfully'})



