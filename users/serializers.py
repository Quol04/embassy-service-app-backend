from rest_framework import serializers
from django.contrib.auth import authenticate
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True,style={'input_type': 'password'})
    
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'username', 'email', 'password', 'phone', 'role', 'date_joined']
        extra_kwargs = {
            'password': {'write_only': True},
            'role': {'default': 'applicant'},
            'date_joined': {'read_only': True}
        }

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            phone=validated_data.get('phone', ''),
            first_name=validated_data.get('first_name', ''),
            last_name=validated_data.get('last_name', ''),
            role=validated_data.get('role', 'applicant'),
            date_joined=validated_data.get('date_joined', None)
        )
        return user
    
class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True,required=True, style={'input_type': 'password'})

    def validate(self, attrs):
        user = authenticate(**attrs)
        if not user:
            raise serializers.ValidationError("Invalid credentials")
        return user
    

class ProfileSerializer(serializers.ModelSerializer):
    class Meta :
        model = User
        fields = ['id','email','username','role','phone','first_name','last_name']
        read_only_fields =['id','email','username','role']
