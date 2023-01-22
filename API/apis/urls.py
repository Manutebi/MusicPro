from collections import namedtuple
from django.urls import path
from django.urls.conf import include
from django.urls.resolvers import URLPattern
from requests.models import parse_header_links
from .views import *    
from django.contrib import admin
from rest_framework import routers




router = routers.DefaultRouter()
router.register('producto',ProductoViewset)


urlpatterns = [

    path('api/', include(router.urls)),

]