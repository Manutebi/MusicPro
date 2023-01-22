import requests
import carro
from django.shortcuts import render
from .carro import Carro
from core.models import categoria, producto
from django.shortcuts import redirect

def eliminar_producto(request, producto_id):
    carro=Carro(request)
    Producto=producto.objects.get(id=producto_id)
    carro.eliminar(Producto=Producto)
    return redirect("cart")

def restar_producto(request, producto_id):
    carro=Carro(request)
    Producto=producto.objects.get(id=producto_id)
    carro.restar_producto(Producto=Producto)
    return redirect("cart")

def limpiar_carro(request):
    carro=Carro(request)
    carro.limpiar_carro()
    return redirect("cart")

def limpiar_carro_producto(request):
    carro=Carro(request)
    carro.limpiar_carro()
    return redirect("listarproductos")

#Los agregados de producto deben tener sus propios views, url's y
#definirlos en "carro" debido a la redireccion que se le debe de dar
def agregar_producto(request, producto_id):
    carro=Carro(request)
    Producto=producto.objects.get(id=producto_id)
    carro.agregar(Producto=Producto)
    return redirect("cart")

def agregar_producto_cuerda(request, producto_id):
    carro=Carro(request)
    Producto=producto.objects.get(id=producto_id)
    carro.agregar_cuerda(Producto=Producto)
    return redirect("prodCuerdas")

def agregar_producto_home(request,producto_id):
    carro=Carro(request)
    Producto = producto.objects.get(id=producto_id)
    carro.agregar(Producto=Producto)
    return redirect("home")


