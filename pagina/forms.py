from django import forms

class agregarProfesorForm(forms.Form) :
    nombre = forms.CharField(max_length=50) 
    legajo = forms.IntegerField()
    
class busquedaProfesorForm(forms.Form) :
    nombre = forms.CharField(max_length=50, required=False) 