from collections import namedtuple
from django.urls import path
from django.urls.conf import include
from requests.models import parse_header_links
from .views import *    
from django.contrib import admin
from rest_framework import routers


#Registros de las apis 
router = routers.DefaultRouter()
router.register('producto', ProductoViewset)
router.register('familia', FamiliaViewset)
router.register('categoria',CategoriaViewset)
router.register('proveedor',ProveedorViewset)






urlpatterns = [
    path('',home, name='home'), 
    #contacto
    path('contacto/', contacto, name="contacto"),
    #producto
    path('agregarproducto/', agregar_producto, name="agregar_producto"),
    path('listarproducto/', listar_productos, name="listar_producto"),
    path('api/producto/<id>/', modificar_producto, name="modificar_producto"),
    path('eliminarproducto/<id>/', eliminar_producto, name="eliminar_producto"),
    #registro
    path('register/', register, name="register"),
    #Categoria
    path('listar_categoria/', listar_categoria, name='listar_categoria' ),
    path('nueva_categoria/', nueva_categoria, name='nueva_categoria'),
    path('modificarcategoria/<id>/', modificar_categoria, name="modificar_categoria"),
    path('eliminarcategoria/<id>/', eliminar_categoria, name="eliminar_categoria"),
    #familia
    path('listar_familias/', listar_familias, name='listar_familias' ),
    path('nueva_familia/', nueva_familia, name='nueva_familia'),
    path('modificarfamilia/<id>/', modificar_familia, name="modificar_familia"),
    path('eliminarfamilia/<id>/', eliminar_familia, name="eliminar_familia"),
    #Proveedor
    path('listar_proveedor/', listar_proveedor, name='listar_proveedor' ),
    path('nuevo_proveedor/', nuevo_proveedor, name='nuevo_proveedor'),
    path('modificarproveedor/<id>/', modificar_proveedor, name="modificar_proveedor"),
    path('eliminarproveedor/<id>/', eliminar_proveedor, name="eliminar_proveedor"),
    #lista de los productos
    path('prodCuerdas/', prodCuerdas, name="prodCuerdas"),
    #carrito
    path('cart/', cart, name="cart"),
    #filtros
    path('prodPianos/', prodPianos, name="prodPianos"),
    path('prodBaterias/', prodBaterias, name="prodBaterias"),
    path('prodAmplificador/', prodAmplificador, name="prodAmplificador"),
    path('accesorios/', accesorios, name="accesorios"),
    #APIS
    path('api/', include(router.urls)),
    path('api2/', include(router.urls)),

    #TBK
    #path('tbk/',tbk,name='tbk'),
    path('tbkRes/', statusTrx, name="tbkRes"),
]