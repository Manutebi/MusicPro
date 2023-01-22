from django.contrib.messages.api import success
from django.core import paginator
from django.db.models.query import RawQuerySet
from django.http import request
from django.http.response import Http404
from django.shortcuts import render, redirect, get_object_or_404
from .models import  *
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth import authenticate,login
from django.db import connection
from rest_framework import viewsets
from .serializers import *
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
# Create your views here.
class ProveedorViewset(viewsets.ModelViewSet):
    queryset = proveedor.objects.all()
    serializer_class = ProveedorSerializer

