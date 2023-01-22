from rest_framework.utils import field_mapping, model_meta
from .models import *
from rest_framework import serializers


class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = producto
        fields = '__all__'


