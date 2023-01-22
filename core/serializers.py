from rest_framework.utils import field_mapping, model_meta
from .models import *
from rest_framework import serializers

class FamiliaSerializer(serializers.ModelSerializer):
    class Meta:
        model = familia
        fields = '__all__'
        
class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = producto
        fields = '__all__'


class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = categoria
        fields = '__all__'

class ProveedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = proveedor
        fields = '__all__'
