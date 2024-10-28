from django.db import models

from django.contrib.auth.models import User # Para importar los usuarios de Django
 # para que no sea accecible por todo los usuarios


# Create your models here.
"""
class cliente(models.Model):
    id_user = models.IntegerField(primary_key=True, unique=True, auto_created=True)
    nombre_usuario = models.CharField(max_length=30,unique=True)
    apellidos = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    passwerd = models.IntegerField(blank=False, null=False, max_length=100)
"""
class Producto(models.Model):
    nombre = models.CharField(max_length=100, null=False, blank=False)
    descripcion = models.TextField(null=True, blank=True)
    precio = models.DecimalField(max_digits=10, decimal_places=0, null=False, blank=False)
    imagen = models.ImageField(upload_to="producto", null=True, blank=True)
    favorito = models.BooleanField(default=False)

    def __str__(self):
        return self.nombre

class Carrito_compra(models.Model):
    cliente = models.ForeignKey(User, on_delete=models.CASCADE) # para que cada vez que se elimine un cliente se elimine su carrito de compras 
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE) 
    # para que dada vez que se elimine un producto se elimine del carrito
    canitdad_producto = models.DecimalField(max_digits=10, decimal_places=0)
    estado = models.BooleanField(default=False,choices= [(False, 'Pendiente'), (True,'Completado')])
    
    """def __str__(self):
        return self.estado"""

    #id_carrito = models.IntegerField(primary_key=True, unique=True, auto_created=True)



"""
class vendedor(models.Model):
    id_vendedor = models.IntegerField(primary_key=True, unique=True, auto_created=True)
    nombre = models.CharField(max_length=30)
    passwerd = models.IntegerField(blank=False, null=False, max_length=100)

class administrado(model.Model):
    id_admin = models.CharField(primary_key=True, unique=True)
    nombre= models.CharField(max_length=30)
    passwerd = models.IntegerField(blank=False, null=False, max_length=100)
"""

"""
python manage.py makemigrations
python manage.py migrate
"""