from django.test.testcases import TestCase
from django.test import TestCase, Client
from django.urls import reverse
from core.models import *
import json

class TestViews(TestCase):
    def test_projet_list_GET(self):
        client = Client()
        response = client.get(reverse('list'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'core/cart.html')