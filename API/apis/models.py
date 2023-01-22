from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.db import models
from django.db.models.base import ModelState
from django.db.models.expressions import Case
from django.db.models.fields import BooleanField, CharField, NullBooleanField
from django.contrib.auth.models import User
from datetime import date,datetime
from django.utils.text import slugify
# Create your models here.



class categoria(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

    def save(self, *args, **kwargs):
        self.slug = slugify(self.nombre)
        super(categoria, self).save(*args, **kwargs)
        
    class Meta:
        managed = False
        db_table = 'core_categoria'        

class familia(models.Model):
    nombre = models.CharField(max_length=50)
    categoria = models.ForeignKey(categoria, on_delete=models.PROTECT)

    def __str__(self):
        return self.nombre
    
    class Meta:
        managed = False
        db_table = 'core_familia'

class proveedor(models.Model):
    rut = models.IntegerField()
    nombre = models.TextField()
    telefono = models.IntegerField()
    rubro = models.TextField()

    def __str__(self):
        return self.nombre 

    class Meta:
        managed = False
        db_table = 'core_proveedor' 
    


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

    def save(self, *args, **kwargs):
        self.slug = slugify(self.nombre)
        super(producto, self).save(*args, **kwargs)   

    class Meta:
        managed = False
        db_table = 'core_producto'