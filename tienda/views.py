from . import models # Para importar mis modelo

from django.http import HttpResponse

from django.shortcuts import render # para renderizar plantillas html, serian las respuestas a las solicitudes HTTP
from django.shortcuts import redirect # con esto puedo rediregir a una url
from django.shortcuts import get_object_or_404 # NO SE
from django.http import JsonResponse# NO SE


from django.contrib.auth.decorators import login_required # con esto puedo generar una necesidad de logeo para acceder a la vista

from django.contrib.auth import logout  # Con esto puedo salir de la cuenta un logout literalmente xd

from .forms import CustomUserCreationForm,ProductoForm # Con esto traigo el archivo formulario que cree para registrarse de django 

from django.contrib.auth import authenticate # Para 
from django.contrib.auth import login # Para que al momento de registrarse tambien se inicie secion

def inicio(request):
    productos = models.Producto.objects.all()
    data = {
        'productos':productos,
    }
    return render(request, 'index.html',data)

def productos(request):
    productos = models.Producto.objects.all()
    data = {
        'form': ProductoForm(), # para hacer el formulario de nuevo producto
        'productos': productos # para sacar todos los productos de la bd
    }
    if request.method == 'POST':
        datos_nuevo_producto = ProductoForm(data=request.POST,files=request.FILES)#CustomUserCreationForm(data=request.POST)
        if datos_nuevo_producto.is_valid():  # verificar si el formulario es valido
            datos_nuevo_producto.save() # para guardar los datos en la base de datos
        
    return render(request, 'productos.html',data)

    

@login_required # con esto, se necesita que el usuario se registre para acceder a esta vista.
def pedido(request):
    carrito_items = models.Carrito_compra.objects.filter(cliente=request.user, estado=False) # no se que hace esto
    productos = models.Producto.objects.all()
    total = sum(item.producto.precio * item.canitdad_producto for item in carrito_items)
    data = {
        'productos': productos,
        'carrito_items': carrito_items,# no se que hace esto
        'total': total,
        
    }
    return render(request, 'pedido.html',data)

@login_required
def agregar_al_carrito(request, producto_id): # no se que hace esto
    producto = get_object_or_404(models.Producto, id=producto_id)
    cliente = request.user

    # Busca si el producto ya está en el carrito
    item_carrito, created = models.Carrito_compra.objects.get_or_create(
        cliente=cliente,
        producto=producto,
        estado=False  # Solo añadir a los pedidos "pendientes"
    )

    # Incrementa la cantidad si el producto ya estaba en el carrito
    if not created:
        item_carrito.canitdad_producto += 1  # o la cantidad deseada
    else:
        item_carrito.canitdad_producto = 1  # Iniciar con 1 si es un nuevo artículo

    item_carrito.save()  # Guarda el objeto en la BD
    return redirect('inicio')

    
@login_required
def eliminar_del_carrito(request, producto_id):
    # Filtra el producto en el carrito para el usuario actual
    item_carrito = models.Carrito_compra.objects.filter(cliente=request.user, producto_id=producto_id, estado=False).first()
    
    # Verifica si el producto está en el carrito
    if item_carrito:
        if item_carrito.canitdad_producto > 1:
            # Disminuye la cantidad en 1 si es mayor a 1
            item_carrito.canitdad_producto -= 1
            item_carrito.save()
        else:
            # Elimina el producto del carrito si la cantidad es 1
            item_carrito.delete()
    return redirect('inicio')
    

def register(request):
    data = {
        'form': CustomUserCreationForm()
    }
    if request.method == 'POST': 
        user_creation_form = CustomUserCreationForm(data=request.POST) # Aqui toma los datos

        if user_creation_form.is_valid(): # Si son correctos los datos entra
            user_creation_form.save() # AQUI guarda los datos del nuevo usuario

            user = authenticate(username=user_creation_form.cleaned_data['username'],password=user_creation_form.cleaned_data['password1']) # verificar que el nombre y pass esten correctos

            login(request, user) # para que se inicie secion automaticamente
            return redirect('/')

    return render(request, 'registration/register.html',data)

def exit(request):
    logout(request) # Esto sirve para salir de la cuenta 
    return redirect('/') # esto sirve para redireccionar al la url inicio


