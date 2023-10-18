from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm, AuthenticationForm
from django.contrib.auth.views import PasswordChangeView
from django import forms
from django.contrib.auth.models import User


class formularioLogin (AuthenticationForm) :
    username = forms.CharField(label='Usuario')
    password = forms.CharField(label='Constraseña', widget=forms.PasswordInput)
    
class formularioDeRegistro(UserCreationForm):
    username = forms.CharField(label='Usuario')
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
        

class formularioCambiarPass (PasswordChangeForm) :
    pass_old = forms.CharField(label='Contraseña vieja', widget = forms.PasswordInput)
    password1 = forms.CharField(label='Nueva contraseña :', widget = forms.PasswordInput)
    password2 = forms.CharField(label='Repetir nueva contraseña :', widget = forms.PasswordInput)

