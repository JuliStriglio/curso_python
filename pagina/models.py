from django.db import models
from ckeditor.fields import RichTextField


class Profesor (models.Model) : 
    nombre = models.CharField(max_length=50)
    legajo = models.IntegerField()
    email = models.EmailField()
    historial = RichTextField(null = True, blank = True)
    fecha_nac = models.DateField(default = '2000-01-01' )
    avatar = models.ImageField(upload_to='avatares', null=True, blank= True)
    link = models.URLField(null=True)
    
    def __str__(self) :
        return f'{self.nombre, self.legajo, self.email}' 
