from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.core.exceptions import ValidationError
import re

class Usuario(AbstractUser):
    """
    Modelo de Usuario personalizado según las especificaciones:
    - Cédula (CharField, primary_key=True, max_length=10)
    - nombre (CharField, max_length=100)
    - contraseña (CharField, max_length=128)
    - email (EmailField, unique=True, max_length=254)
    """
    
    # Usar cédula como primary key en lugar de username
    cedula = models.CharField(
        primary_key=True,
        max_length=10,
        validators=[
            MinLengthValidator(8, "La cédula debe tener al menos 8 caracteres"),
            MaxLengthValidator(10, "La cédula no puede tener más de 10 caracteres")
        ],
        help_text="Cédula de identidad del usuario"
    )
    
    nombre = models.CharField(
        max_length=100,
        help_text="Nombre completo del usuario"
    )
    
    email = models.EmailField(
        unique=True,
        max_length=254,
        help_text="Correo electrónico único del usuario"
    )
    
    # Usar el campo password heredado de AbstractUser
    
    # Campos adicionales para tracking
    fecha_registro = models.DateTimeField(auto_now_add=True)
    fecha_ultimo_acceso = models.DateTimeField(auto_now=True)
    activo = models.BooleanField(default=True)
    
    # Configuración del modelo
    USERNAME_FIELD = 'cedula'
    REQUIRED_FIELDS = ['nombre', 'email']
    
    class Meta:
        db_table = 'usuarios'
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'
        ordering = ['nombre']
    
    def __str__(self):
        return f"{self.nombre} ({self.cedula})"
    
    def clean(self):
        """Validación personalizada del modelo"""
        super().clean()
        
        # Validar formato de cédula (solo números)
        if self.cedula and not re.match(r'^\d+$', self.cedula):
            raise ValidationError({
                'cedula': 'La cédula debe contener solo números'
            })
    
    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)
    
    @property
    def username(self):
        """Mantener compatibilidad con AbstractUser usando cédula como username"""
        return self.cedula 