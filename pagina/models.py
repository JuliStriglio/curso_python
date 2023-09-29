from django.db import models

# Create your models here.

class Profesor (models.Model) : 
    nombre = models.CharField(max_length=50)
    legajo = models.IntegerField()
    
    def __str__(self) :
        return f'{self.nombre, self.legajo}' 
