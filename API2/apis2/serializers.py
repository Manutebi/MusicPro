from rest_framework.utils import field_mapping, model_meta
from .models import *
from rest_framework import serializers


class ProveedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = proveedor
        fields = '__all__'


