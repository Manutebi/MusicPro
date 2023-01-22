from django.db import models
from django.db.models.base import ModelState
from django.db.models.expressions import Case
from django.db.models.fields import BooleanField, CharField, NullBooleanField
from django.contrib.auth.models import User
from datetime import date,datetime
from django.utils.text import slugify
from API2.apis2.models import proveedor
from API.apis.models import categoria
#Create your models here

class categoria(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

    def save(self, *args, **kwargs):
        self.slug = slugify(self.nombre)
        super(categoria, self).save(*args, **kwargs)    

class familia(models.Model):
    nombre = models.CharField(max_length=50)
    categoria = models.ForeignKey(categoria, on_delete=models.PROTECT)

    def __str__(self):
        return self.nombre

class proveedor(models.Model):
    rut = models.IntegerField()
    nombre = models.TextField()
    telefono = models.IntegerField()
    rubro = models.TextField()

    def __str__(self):
        return self.nombre      

class producto(models.Model):
    nombre = models.CharField(max_length=30)
    descripcion = models.TextField(max_length=300)
    precio = models.IntegerField() 
    familia = models.ForeignKey(familia, on_delete=models.PROTECT)
    vencimiento = models.DateField()
    stock = models.IntegerField()
    stock_critico = models.IntegerField()
    proveedor = models.ForeignKey(proveedor, on_delete=models.PROTECT)
    imagen = models.ImageField(upload_to='productos', null=True)
    oferta = models.BooleanField(default='0', null=False)

    def __str__(self):
        return self.nombre

class cargo(models.Model):
    nombre = models.CharField(max_length=20)
    descripcio = models.TextField()

class persona(models.Model):
    rut = models.IntegerField()
    nombre = models.TextField()
    telefono = models.IntegerField()
    cargo = models.ForeignKey(cargo, on_delete=models.PROTECT)
    User = models.ForeignKey(User, on_delete=models.CASCADE,null=False,default=None)
    def __str__(self):
        return self.nombre

opciones_consultas = [

    [0, 'Consulta'],
    [1, 'Reclamo'],
    [2, 'Sugerencia'],
    [3, 'Felicitaciones'],
    [4, 'Solicitud de Proveedor']]

class contacto(models.Model):
    nombre = models.CharField(max_length=50)
    correo = models.EmailField()
    tipo_consulta = models.IntegerField(choices=opciones_consultas)
    mensaje = models.TextField()

    def __str__(self):
        return self.nombre

class factura(models.Model): 
    fecha = models.DateField(default=datetime.today)
    producto = models.ForeignKey(producto, on_delete=models.CASCADE)
    canitdad_producto = models.IntegerField()
    total = models.IntegerField()

    def __str__(self):
        return self.id

class boleta(models.Model):
    fecha = models.DateField(default=datetime.today)
    producto = models.ForeignKey(producto, on_delete=models.CASCADE)
    canitdad_producto = models.IntegerField()
    total = models.IntegerField()

    def __str__(self):
        return self.id

class cliente(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    nombre = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.nombre

class orden(models.Model):
    cliente = models.ForeignKey(cliente, on_delete=models.SET_NULL, null=True, blank=True)
    orden_fecha = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False)
    transaccion_id = models.CharField(max_length=100, null=True)

    def __str__(self):
        return str(self.id)

    @property
    def get_cart_total(self):
        ordenitems = self.ordenitem_set.all()
        total = sum([item.get_total for item in ordenitems])
        return total
    
    @property
    def get_cart_items(self):
        ordenitems = self.ordenitem_set.all()
        total = sum([item.cantidad for item in ordenitems])
        return total

class ordenItem(models.Model):
    producto = models.ForeignKey(producto, on_delete=models.SET_NULL, null=True)
    orden = models.ForeignKey(orden, on_delete=models.SET_NULL, null=True)
    cantidad = models.IntegerField(default=0, null=True, blank=True)
    fecha_agregada = models.DateTimeField(auto_now_add=True)

    @property
    def get_total(self):
        total = self.producto.precio * self.cantidad
        return total

class direccion_envio(models.Model):
    cliente = models.ForeignKey(cliente, on_delete=models.SET_NULL, null=True)
    orden = models.ForeignKey(orden, on_delete=models.SET_NULL, null=True)
    direccion = models.CharField(max_length=200, null=False)
    ciudad = models.CharField(max_length=200, null=False)
    Region = models.CharField(max_length=200, null=False)
    codigo_postal = models.CharField(max_length=200, null=False)
    fecha_agregada = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.direccion