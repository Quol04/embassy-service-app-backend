from rest_framework import serializers
from .models import Service


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model= Service
        fields= ['id','name','description','fee','is_active','updated_at','created_at']