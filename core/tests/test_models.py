from core.models import categoria
from django.test import TestCase
from core.models import *

#
class Tesmtodels(TestCase):

    def setUp(self):
        self.categoria1 = categoria.objects.create(
            nombre = 'proyecto'
        )

   
