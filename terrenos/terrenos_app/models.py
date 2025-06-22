from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.exceptions import ValidationError

class Finca(models.Model):
    """
    Modelo Finca según las especificaciones:
    - id_productor (ForeignKey(Usuario, to_field="Cédula", on_delete=CASCADE), primary_key=True, max_length=10)
    - nombre_finca (CharField, primary_key=True, max_length=100)
    - ubicación (CharField, max_length=200)
    - tipo_de_suelo (CharField, max_length=50)
    - fecha_registro_finca (DateTimeField)
    """
    
    # Clave primaria compuesta: id_productor + nombre_finca
    id_productor = models.CharField(max_length=10, help_text="Cédula del productor")
    nombre_finca = models.CharField(max_length=100, help_text="Nombre de la finca")
    ubicacion = models.CharField(max_length=200, help_text="Ubicación de la finca")
    tipo_de_suelo = models.CharField(max_length=50, help_text="Tipo de suelo de la finca")
    fecha_registro_finca = models.DateTimeField(auto_now_add=True, help_text="Fecha de registro de la finca")
    
    class Meta:
        db_table = 'fincas'
        verbose_name = 'Finca'
        verbose_name_plural = 'Fincas'
        # Clave primaria compuesta
        unique_together = ('id_productor', 'nombre_finca')
        ordering = ['id_productor', 'nombre_finca']
    
    def __str__(self):
        return f"{self.nombre_finca} - Productor: {self.id_productor}"
    
    def clean(self):
        """Validación personalizada del modelo"""
        super().clean()
        
        # Validar que el id_productor contenga solo números
        if self.id_productor and not self.id_productor.isdigit():
            raise ValidationError({
                'id_productor': 'El ID del productor debe contener solo números'
            })

class Parcela(models.Model):
    """
    Modelo Parcela según las especificaciones:
    - id_productor_p (ForeignKey(Finca, to_field="id_productor", on_delete=CASCADE), primary_key=True, max_length=10)
    - nombre_finca_p (ForeignKey(Finca, to_field="nombre_finca", on_delete=CASCADE), primary_key=True, max_length=100)
    - id_parcela (CharField, primary_key=True, max_length=20)
    - superficie (FloatField, min_value=0, max_value=10000)
    """
    
    # Clave primaria compuesta: id_productor_p + nombre_finca_p + id_parcela
    id_productor_p = models.CharField(max_length=10, help_text="Cédula del productor")
    nombre_finca_p = models.CharField(max_length=100, help_text="Nombre de la finca")
    id_parcela = models.CharField(max_length=20, help_text="Identificador único de la parcela")
    superficie = models.FloatField(
        validators=[
            MinValueValidator(0, "La superficie debe ser mayor a 0"),
            MaxValueValidator(10000, "La superficie no puede ser mayor a 10,000")
        ],
        help_text="Superficie de la parcela en hectáreas"
    )
    
    class Meta:
        db_table = 'parcelas'
        verbose_name = 'Parcela'
        verbose_name_plural = 'Parcelas'
        # Clave primaria compuesta
        unique_together = ('id_productor_p', 'nombre_finca_p', 'id_parcela')
        ordering = ['id_productor_p', 'nombre_finca_p', 'id_parcela']
    
    def __str__(self):
        return f"Parcela {self.id_parcela} - Finca: {self.nombre_finca_p} - Productor: {self.id_productor_p}"
    
    def clean(self):
        """Validación personalizada del modelo"""
        super().clean()
        
        # Validar que el id_productor_p contenga solo números
        if self.id_productor_p and not self.id_productor_p.isdigit():
            raise ValidationError({
                'id_productor_p': 'El ID del productor debe contener solo números'
            })
        
        # Validar que la parcela pertenezca a una finca existente
        if self.id_productor_p and self.nombre_finca_p:
            try:
                Finca.objects.get(
                    id_productor=self.id_productor_p,
                    nombre_finca=self.nombre_finca_p
                )
            except Finca.DoesNotExist:
                raise ValidationError({
                    'nombre_finca_p': 'La finca especificada no existe para este productor'
                })
    
    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

class Cultivo(models.Model):
    """
    Modelo Cultivo según las especificaciones:
    - id_finca (ForeignKey(Finca), primary_key=True)
    - tipo_cultivo (CharField, max_length=50)
    - area_cultivo (FloatField, min_value=0.01, max_value=10000)
    - fecha_siembra (DateField)
    - fecha_cosecha (DateField)
    - estado_cultivo (CharField, max_length=20)
    """
    
    id_finca = models.ForeignKey(Finca, on_delete=models.CASCADE, help_text="Finca donde se cultiva")
    tipo_cultivo = models.CharField(max_length=50, help_text="Tipo de cultivo")
    area_cultivo = models.FloatField(
        validators=[
            MinValueValidator(0.01, "El área debe ser mayor a 0.01"),
            MaxValueValidator(10000, "El área no puede ser mayor a 10,000")
        ],
        help_text="Área de cultivo en hectáreas"
    )
    fecha_siembra = models.DateField(help_text="Fecha de siembra")
    fecha_cosecha = models.DateField(help_text="Fecha de cosecha")
    estado_cultivo = models.CharField(max_length=20, help_text="Estado actual del cultivo")
    
    class Meta:
        db_table = 'cultivos'
        verbose_name = 'Cultivo'
        verbose_name_plural = 'Cultivos'
        ordering = ['id_finca', 'tipo_cultivo']
    
    def __str__(self):
        return f"{self.tipo_cultivo} - Finca: {self.id_finca.nombre_finca} - Área: {self.area_cultivo} ha"
    
    def clean(self):
        """Validación personalizada del modelo"""
        super().clean()
        
        # Validar que fecha_cosecha sea posterior a fecha_siembra
        if self.fecha_cosecha and self.fecha_siembra and self.fecha_cosecha <= self.fecha_siembra:
            raise ValidationError({
                'fecha_cosecha': 'La fecha de cosecha debe ser posterior a la fecha de siembra'
            })
    
    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs) 