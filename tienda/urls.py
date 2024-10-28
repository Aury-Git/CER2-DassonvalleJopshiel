from django.urls import path, include
from . import views


from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('productos/',views.productos, name= 'productos'),
    path('carrito_compras/',views.pedido, name= 'carrito'),
    path('accounts/', include('django.contrib.auth.urls')), # vistas de django
    path('logout/',views.exit, name= 'exit'),# salir
    path('register/',views.register, name= 'register'), # registrarse

    path('agregar_producto/<int:producto_id>/', views.agregar_al_carrito, name='agregar_producto'),
    path('eliminar_producto/<int:producto_id>/', views.eliminar_del_carrito, name='eliminar_producto'),
]
