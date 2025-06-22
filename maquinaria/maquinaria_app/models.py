from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Maquinaria(models.Model):
    """
    Modelo Maquinaria según las especificaciones:
    - id_maquinaria (CharField, primary_key=True, max_length=20)
    - propietario_m (ForeignKey(Usuario, to_field="Cédula", on_delete=CASCADE), max_length=10)
    - tipo (CharField, max_length=50)
    - marca (CharField, max_length=50)
    - modelo (CharField, max_length=50)
    - año (IntegerField, min_value=1900, max_value=2100)
    """
    
    id_maquinaria = models.CharField(primary_key=True, max_length=20, help_text="Identificador único de la maquinaria")
    propietario_m = models.CharField(max_length=10, help_text="Cédula del propietario")
    tipo = models.CharField(max_length=50, help_text="Tipo de maquinaria")
    marca = models.CharField(max_length=50, help_text="Marca de la maquinaria")
    modelo = models.CharField(max_length=50, help_text="Modelo de la maquinaria")
    año = models.IntegerField(
        validators=[
            MinValueValidator(1900, "El año debe ser mayor o igual a 1900"),
            MaxValueValidator(2100, "El año no puede ser mayor a 2100")
        ],
        help_text="Año de fabricación"
    )
    
    class Meta:
        db_table = 'maquinaria'
        verbose_name = 'Maquinaria'
        verbose_name_plural = 'Maquinaria'
        ordering = ['propietario_m', 'tipo', 'marca']
    
    def __str__(self):
        return f"{self.marca} {self.modelo} ({self.id_maquinaria}) - Propietario: {self.propietario_m}"

class VentaMaquinaria(models.Model):
    """
    Modelo Venta de Maquinaria según las especificaciones:
    - id_maquinaria (ForeignKey(Maquinaria, to_field="id_maquinaria", on_delete=CASCADE), max_length=20)
    - propietario_v (ForeignKey(Usuario, to_field="Cédula", on_delete=CASCADE), max_length=10)
    - id_listado_v (CharField, primary_key=True, max_length=20)
    - fecha_v (DateField)
    - precio (FloatField, min_value=0, max_value=1000000)
    """
    
    id_listado_v = models.CharField(primary_key=True, max_length=20, help_text="Identificador único del listado de venta")
    id_maquinaria = models.CharField(max_length=20, help_text="ID de la maquinaria")
    propietario_v = models.CharField(max_length=10, help_text="Cédula del propietario")
    fecha_v = models.DateField(help_text="Fecha de publicación de la venta")
    precio = models.FloatField(
        validators=[
            MinValueValidator(0, "El precio debe ser mayor o igual a 0"),
            MaxValueValidator(1000000, "El precio no puede ser mayor a 1,000,000")
        ],
        help_text="Precio de venta"
    )
    
    class Meta:
        db_table = 'venta_maquinaria'
        verbose_name = 'Venta de Maquinaria'
        verbose_name_plural = 'Ventas de Maquinaria'
        ordering = ['-fecha_v']
    
    def __str__(self):
        return f"Venta {self.id_listado_v} - Maquinaria: {self.id_maquinaria} - Precio: ${self.precio}"

class ReservaMaquinaria(models.Model):
    """
    Modelo Reserva Maquinaria según las especificaciones:
    - id_maquinaria (ForeignKey(Maquinaria, to_field="id_maquinaria", on_delete=CASCADE), max_length=20)
    - propietario_r (ForeignKey(Usuario, to_field="Cédula", on_delete=CASCADE), max_length=10)
    - id_listado_r (CharField, primary_key=True, max_length=20)
    - fecha_inicio (DateField)
    - fecha_fin (DateField)
    """
    
    id_listado_r = models.CharField(primary_key=True, max_length=20, help_text="Identificador único del listado de reserva")
    id_maquinaria = models.CharField(max_length=20, help_text="ID de la maquinaria")
    propietario_r = models.CharField(max_length=10, help_text="Cédula del propietario")
    fecha_inicio = models.DateField(help_text="Fecha de inicio de la reserva")
    fecha_fin = models.DateField(help_text="Fecha de fin de la reserva")
    
    class Meta:
        db_table = 'reserva_maquinaria'
        verbose_name = 'Reserva de Maquinaria'
        verbose_name_plural = 'Reservas de Maquinaria'
        ordering = ['fecha_inicio']
    
    def __str__(self):
        return f"Reserva {self.id_listado_r} - Maquinaria: {self.id_maquinaria} - {self.fecha_inicio} a {self.fecha_fin}"
    
    def clean(self):
        """Validar que fecha_fin sea posterior a fecha_inicio"""
        from django.core.exceptions import ValidationError
        if self.fecha_fin and self.fecha_inicio and self.fecha_fin <= self.fecha_inicio:
            raise ValidationError({
                'fecha_fin': 'La fecha de fin debe ser posterior a la fecha de inicio'
            }) 