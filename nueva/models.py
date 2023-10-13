from django.db import models

class Materia (models.Model) :
    nombre = models.CharField(max_length=50)
    dia_cursado = models.CharField(max_length=50)
    descripcion = models.TextField()
    fecha_parcial = models.DateField()
    
    def __str__(self) :
        return f'{self.nombre}'
