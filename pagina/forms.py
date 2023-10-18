from django import forms

class agregarProfesorForm(forms.Form) :
    nombre = forms.CharField(max_length=50) 
    legajo = forms.IntegerField()
    email = forms.EmailField()
    fecha_nac = forms.DateField()
    avatar = forms.ImageField(required=False)
    link = forms.URLField(required=False)
    
class busquedaProfesorForm(forms.Form) :
    nombre = forms.CharField(max_length=50, required=False) 
    
class editarProfesorFormulario(forms.Form):
     nombre = forms.CharField(max_length=50) 
     legajo = forms.IntegerField()
     email = forms.EmailField()
     fecha_nac = forms.DateField()
     avatar = forms.ImageField(required=False)
     link = forms.URLField(required=False)

    