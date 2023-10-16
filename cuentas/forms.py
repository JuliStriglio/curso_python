from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.views import PasswordChangeView
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
    link = forms.URLField(required=False)
    avatar= forms.ImageField(required=False)
    
    class Meta :
        model = User
        fields = ['email', 'first_name', 'last_name', 'link', 'avatar']
        

class formularioCambiarPass (PasswordChangeView):
    old_pass = forms.CharField(label='Contraseña vieja', widget = forms.PasswordInput)
    password1 = forms.CharField(label='Contraseña nueva', widget = forms.PasswordInput)
    password1 = forms.CharField(label='Repetir contraseña nueva', widget = forms.PasswordInput)
    
    class Meta :
        model = User 
        fields = ['old_pass', 'password1', 'password2']
        help_texts = {campo : '' for campo in fields}