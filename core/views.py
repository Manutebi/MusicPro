import carro
from django.contrib.messages.api import success
from django.core import paginator
from django.db.models.query import RawQuerySet
from django.http import request
from django.http.response import Http404
from django.shortcuts import render, redirect, get_object_or_404
from .models import  *
from .forms import *
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth import authenticate, login
from django.db import connection
from rest_framework import viewsets
from .serializers import *
from django.http import JsonResponse
from .services import *
from django.views.decorators.csrf import csrf_exempt
from carro.context_processor import *
from IWFF.settings import TEMPLATES
import json
# Create your views here.


#Home de la pagina
def home(request):
    data = {
        'listado': get_productos()
    }
    return render(request, 'core/home.html', data)

#formulario de contacto
def contacto(request):
    data = {
        'form': ContactoForms()
    }
    if request.method == 'POST':
        formulario = ContactoForms(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "contacto guardado"
        else:
            data["form"] = formulario
    return render(request, 'core/Contacto.html',data)


#Productos
#Procedimiento para agregar producto
def agregar_producto(request):

    data = {
        'form': AgregarProductoForms()  
    }
    if request.method == 'POST':
        formulario = AgregarProductoForms(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Producto registrado correctamente ")
        else:
            data["form"] = formulario
            messages.warning(request, "ERROR: El producto no fue registrado")

    return render(request, 'core/producto/agregar.html', data)
#Funcion listar prodcutos
def listar_productos(request):
    productos = producto.objects.all().order_by('id')
    data = {
        'producto':productos,
    }
    return render(request, 'core/producto/listar.html',data)
#Procedimiento para modificar producto
def modificar_producto(request, id):
    product = get_object_or_404(producto, id=id)
    data = {
        'form': AgregarProductoForms(instance=product)
    }
    if request.method == 'POST':
        formulario = AgregarProductoForms(data=request.POST,instance=product, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, " Producto modificado correctamente ")
            return redirect(to="listar_producto")
        else:
            data["form"] = formulario
            
    return render(request, 'core/producto/modificar.html', data)
#Procedimiento para eliminar producto
def eliminar_producto(request, id ):
    prod = get_object_or_404(producto, id=id)
    prod.delete()
    messages,success(request, "Producto eliminado correctamente")
    return redirect(to="listar_producto")
#Registro de clientes
def register(request):
    data = {
        'form':RegistroForms()
    }
    if request.method == 'POST':
        formulario = RegistroForms(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"],password=formulario.cleaned_data["password1"])
            login(request, user)
            messages.success(request, "Registro exitoso")
            return redirect(to="home")
        data['from'] = formulario
    return render(request, 'registration/register.html', data)

#Categorias
#Funcion listar categorias
def listar_categoria(request):
    data = {
        'categoria':get_categoria()
    }
    return render(request, 'core/categorias/listar.html', data)
#funcion de almacenado de categoria
@csrf_exempt
def nueva_categoria(request):
    data = {
    }
    if request.method == 'POST':
        nombre = request.POST.get('nombreCategoria')
        salida = post_categoria(nombre)
        messages,success(request, "categoria agregada correctamente")
    return render(request, 'core/categorias/agregar.html', data)
#Procedimiento para eliminar categoria    
def eliminar_categoria(request, id ):
    delete_categoria(id=id)
    messages,success(request, "categoria eliminada correctamente")
    return redirect(to="listar_categoria")
#Procedimiento para modificar categoria
def modificar_categoria(request, id):
    categ = get_object_or_404(categoria, id=id)
    data = {
        'form': AgregarCategoriaForms(instance=categ)
    }
    if request.method == 'POST':
        formulario = AgregarCategoriaForms(data=request.POST,instance=categ)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, " Categoria modificada correctamente ")
            return redirect(to="listar_categoria")
        else:
            data["form"] = formulario
            
    return render(request, 'core/categorias/modificar.html', data)

#Familias
#Funcion listar familias
def listar_familias(request):
    familias = familia.objects.all().order_by('id')
    data = {
        'familia':familias
    }
    return render(request, 'core/familia/listar.html', data)
#funcion de almacenado de familias
def nueva_familia(request):

    data = {
        'form': AgregarFamiliaForms()  
    }
    if request.method == 'POST':
        formulario = AgregarFamiliaForms(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Familia registrada correctamente ")
        else:
            data["form"] = formulario
            messages.warning(request, "ERROR: La familia no fue registrada")

    return render(request, 'core/familia/agregar.html', data)
#Procedimiento para eliminar familia    
def eliminar_familia(request, id ):
    fam = get_object_or_404(familia, id=id)
    fam.delete()
    messages,success(request, "familia eliminado correctamente")
    return redirect(to="listar_familias")
#Procedimiento para modificar familia
def modificar_familia(request, id):
    famil = get_object_or_404(familia, id=id)
    data = {
        'form': AgregarFamiliaForms(instance=famil)
    }
    if request.method == 'POST':
        formulario = AgregarFamiliaForms(data=request.POST,instance=famil)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, " Familia modificada correctamente ")
            return redirect(to="listar_familias")
        else:
            data["form"] = formulario
            
    return render(request, 'core/familia/modificar.html', data)

#Proveedores 
#Funcion de listado de proveedores
def listar_proveedor (request):
     
    data = {
        'proveedor':get_proveedor()
    }
    return render(request,'core/proveedor/listar.html',data)
#Funcion de almacenado de proveedor
def nuevo_proveedor(request):
    data = {
        'form': AgregarProveedorForms()  
    }
    if request.method == 'POST':
        formulario = AgregarProveedorForms(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, " Proveedor registrado correctamente ")
        else:
            data["form"] = formulario
            messages.warning(request, "ERROR: El proveedor no fue registrado")

    return render(request, 'core/proveedor/agregar.html', data)
#Procedimiento para eliminar proveedor
def eliminar_proveedor(request, id ):
    prov = get_object_or_404(proveedor, id=id)
    prov.delete()
    messages,success(request, "Proveedor eliminado correctamente")
    return redirect(to="listar_proveedor")
#Procedimiento modificar Proveedor 
def modificar_proveedor(request, id):
    prov = get_object_or_404(proveedor, id=id)
    data = {
        'form': AgregarProveedorForms(instance=prov)
    }
    if request.method == 'POST':
        formulario = AgregarProveedorForms(data=request.POST,instance=prov)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, " Proveedor modificada correctamente ")
            return redirect(to="listar_proveedor")
        else:
            data["form"] = formulario
            
    return render(request, 'core/proveedor/modificar.html', data)

#TIENDA
@csrf_exempt
def cart(request):
    monto = request.POST.get('precio_total')
    data = {
        'producto': get_productos(),
        'resultado': get_initTrxTBK(monto),
    }
    data['mensaje']=(monto)
    return render(request, 'core/cart.html', data)
#Listado de productos de cuerdas
def prodCuerdas(request):
    data = {
        'producto': get_productos()
    }
    return render(request, 'core/prodCuerdas.html', data)
#Listado de productos de pianos
def prodPianos(request):
    data = {
        'producto': get_productos()
    }
    return render(request, 'core/prodPianos.html', data)

     #Listado de productos de baterias
def prodBaterias(request):
    data = {
        'producto': get_productos()
    }
    return render(request, 'core/prodBaterias.html', data)

    #Listado de productos de Amplificadores
def prodAmplificador(request):
    data = {
        'producto': get_productos()
    }
    return render(request, 'core/prodAmplificador.html', data)

    #Listado de productos de Accesorios
def accesorios(request):
    data = {
        'producto': get_productos()
    }
    return render(request, 'core/accesorios.html', data)

#Serializers
#Producto serializer
class ProductoViewset(viewsets.ModelViewSet):
    queryset = producto.objects.all()
    serializer_class = ProductoSerializer
#Familia
class FamiliaViewset(viewsets.ModelViewSet):
    queryset = familia.objects.all()
    serializer_class = FamiliaSerializer
#Categoria
class CategoriaViewset(viewsets.ModelViewSet):
    queryset = categoria.objects.all()
    serializer_class = CategoriaSerializer
#Proveedor
class ProveedorViewset(viewsets.ModelViewSet):
    queryset = proveedor.objects.all()
    serializer_class = ProveedorSerializer
#TBK
@csrf_exempt
def statusTrx(request):
    data = {
        'resultado': get_statusTBK(request),
    }
    return render(request, 'core/tbk/statusTbk.html',data)