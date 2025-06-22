from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Usuario

@admin.register(Usuario)
class UsuarioAdmin(UserAdmin):
    list_display = ('cedula', 'nombre', 'email', 'activo', 'fecha_registro')
    list_filter = ('activo', 'fecha_registro')
    search_fields = ('cedula', 'nombre', 'email')
    ordering = ('nombre',)
    
    fieldsets = (
        (None, {'fields': ('cedula', 'password')}),
        ('Información Personal', {'fields': ('nombre', 'email')}),
        ('Permisos', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Fechas importantes', {'fields': ('last_login', 'date_joined')}),
    )
    
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('cedula', 'nombre', 'email', 'password1', 'password2'),
        }),
    ) 