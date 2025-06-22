from rest_framework import serializers
from .models import Usuario

class UsuarioSerializer(serializers.ModelSerializer):
    """Serializer para el modelo Usuario"""
    
    class Meta:
        model = Usuario
        fields = ['cedula', 'nombre', 'email', 'fecha_registro']
        read_only_fields = ['fecha_registro']

class UsuarioSignupSerializer(serializers.ModelSerializer):
    """Serializer para registro de usuarios"""
    password = serializers.CharField(write_only=True, min_length=6)
    password_confirm = serializers.CharField(write_only=True)
    
    class Meta:
        model = Usuario
        fields = ['cedula', 'nombre', 'email', 'password', 'password_confirm']
    
    def validate(self, attrs):
        """Validar que las contraseñas coincidan"""
        if attrs['password'] != attrs['password_confirm']:
            raise serializers.ValidationError("Las contraseñas no coinciden")
        return attrs
    
    def create(self, validated_data):
        """Crear usuario con contraseña hasheada"""
        validated_data.pop('password_confirm')
        password = validated_data.pop('password')
        user = Usuario(**validated_data)
        user.set_password(password)
        user.save()
        return user

class UsuarioLoginSerializer(serializers.Serializer):
    """Serializer para login de usuarios"""
    email = serializers.EmailField()
    password = serializers.CharField()

class UsuarioResponseSerializer(serializers.ModelSerializer):
    """Serializer para respuesta de usuario (sin contraseña)"""
    
    class Meta:
        model = Usuario
        fields = ['cedula', 'nombre', 'email', 'fecha_registro'] 