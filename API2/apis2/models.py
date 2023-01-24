from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.db import models
from django.db.models.base import ModelState
from django.db.models.expressions import Case
from django.db.models.fields import BooleanField, CharField, NullBooleanField
from django.contrib.auth.models import User
from datetime import date,datetime
from django.utils.text import slugify
# Create your models here.


class proveedor(models.Model):
    rut = models.IntegerField()
    nombre = models.TextField()
    telefono = models.IntegerField()
    rubro = models.TextField()

    def __str__(self):
        return self.nombre      

    def save(self, *args, **kwargs):
        self.slug = slugify(self.nombre)
        super(proveedor, self).save(*args, **kwargs)

    class Meta:
        managed = False
        db_table = 'core_proveedor'


