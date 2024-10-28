# LA IDEA DE ESTE FORMULARIO ES UTILIZAR EL SISTEMA DE REGISTRACION QUE TRAE DJANGO

from django import forms
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.models import User # Para traer el modelo de django de usuario

from .models import Producto


class CustomUserCreationForm(UserCreationForm): # NO SE como lo hace pero crea un sistema de registro
    class Meta:
        model = User
        fields = ['username','email','password1','password2']


class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'descripcion', 'precio', 'imagen']