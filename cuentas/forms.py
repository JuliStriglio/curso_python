from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from django.contrib.auth.models import User

class formularioDeRegistro(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label='Contraseña', widget = forms.PasswordInput)
    password2 = forms.CharField(label='Repetir contraseña', widget = forms.PasswordInput)
    
    class Meta :
        model = User 
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {campo : '' for campo in fields}
        

class formularioDeEditarPerfil (UserChangeForm):
    password = None
    email = forms.EmailField(label='Cambiar email')
    first_name = forms.CharField(max_length=30, label='Nombre')
    last_name = forms.CharField(max_length=50, label='Apellido')
   # link = forms.URLField(required=False)
   # avatar= forms.ImageField(required=False)
    
    class Meta :
        model = User
        fields = ['email', 'first_name', 'last_name']