from django.db import models
from ckeditor.fields import RichTextField

class Materia (models.Model) :
    nombre = models.CharField(max_length=50)
    dia_cursado = models.CharField(max_length=50)
    descripcion = RichTextField()
    fecha_parcial = models.DateField()
    
    def __str__(self) :
        return f'{self.nombre}'
