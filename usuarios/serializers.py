from rest_framework import serializers
from .models import Usuario
from django.core.exceptions import ValidationError

class UsuarioSerializer(serializers.ModelSerializer):

    class Meta:
        model = Usuario
        """Campos que se incluyen en el serializador"""
        fields = ["id", "email", "first_name",'password']
        extra_kwargs = {'password': {'write_only': True}}
    
    def validate_email(self, value):
        value = value.lower()

        if Usuario.objects.filter(email=value).exists():
            raise ValidationError("El correo electrónico ya está registrado.")
        
        return value

class UsuarioUpdateSerializer(serializers.ModelSerializer):
     class Meta:
        model = Usuario
        """Campos que se incluyen en el serializador"""
        fields = ["id", "email", "first_name"]