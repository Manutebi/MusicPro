from django.contrib import admin
from .models import *
# Register your models here.

#
class ProductoAdmin(admin.ModelAdmin):
    list_display = ['nombre','descripcion','precio','vencimiento', 'stock', 'stock_critico']
    list_editable = ['precio']
    search_fields = ['nombre', 'stock']
    list_filter = ['stock','familia']
    list_per_page = 50

class CargoAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'descripcio']

class ProveedorAdmin(admin.ModelAdmin):
    list_display = ['rut', 'nombre', 'telefono', 'rubro']



#Muestra tabla en admin para su edición
admin.site.register(categoria)
admin.site.register(familia)
admin.site.register(proveedor, ProveedorAdmin)
admin.site.register(producto, ProductoAdmin)
admin.site.register(cargo, CargoAdmin)
admin.site.register(contacto)
admin.site.register(orden)
admin.site.register(ordenItem)
admin.site.register(direccion_envio)
