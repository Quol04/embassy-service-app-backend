from django.db import models

# Create your models here.
class Service(models.Model):
    name= models.CharField(max_length=200, unique=True)
    description= models.TextField(blank=True)
    fee= models.DecimalField(max_digits=10, decimal_places=2)
    is_active= models.BooleanField(default=True)
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} - ${self.fee}"
    
