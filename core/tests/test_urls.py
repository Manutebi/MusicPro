from django.test import SimpleTestCase
from django.urls import reverse, resolve
from core.views import * 

class TestUrls(SimpleTestCase):
    def test_home_url_is_resolved(self):
        url = reverse('home')
        self.assertEquals(resolve(url).func, home)

    def test_contacto_url_is_resolved(self):
        url = reverse('contacto')
        self.assertEquals(resolve(url).func, contacto)
    
    def test_agregar_producto_is_resolved(self):
        url = reverse('agregar_producto')
        self.assertEquals(resolve(url).func, agregar_producto)

    def test_register_is_resolved(self):
        url = reverse('register')
        self.assertEquals(resolve(url).func, register)

    def test_listar_categoria_is_resolved(self):
        url = reverse('listar_categoria')
        self.assertEquals(resolve(url).func, listar_categoria)

    def test_nueva_categoria_is_resolved(self):
        url = reverse('nueva_categoria')
        self.assertEquals(resolve(url).func, nueva_categoria)

    def test_listar_familias_is_resolved(self):
        url = reverse('listar_familias')
        self.assertEquals(resolve(url).func, listar_familias)

    def test_nueva_familia_is_resolved(self):
        url = reverse('nueva_familia')
        self.assertEquals(resolve(url).func, nueva_familia)

    def test_listar_proveedor_is_resolved(self):
        url = reverse('listar_proveedor')
        self.assertEquals(resolve(url).func, listar_proveedor)

    def test_nuevo_proveedor_is_resolved(self):
        url = reverse('nuevo_proveedor')
        self.assertEquals(resolve(url).func, nuevo_proveedor)

    def test_prodCuerdas_is_resolved(self):
        url = reverse('prodCuerdas')
        self.assertEquals(resolve(url).func, prodCuerdas)

    def test_cart_is_resolved(self):
        url = reverse('cart')
        self.assertEquals(resolve(url).func, cart)

    def test_prodPianos_is_resolved(self):
        url = reverse('prodPianos')
        self.assertEquals(resolve(url).func, prodPianos)

    def test_prodBaterias_is_resolved(self):
        url = reverse('prodBaterias')
        self.assertEquals(resolve(url).func, prodBaterias)

    def test_prodAmplificador_is_resolved(self):
        url = reverse('prodAmplificador')
        self.assertEquals(resolve(url).func, prodAmplificador)

    def test_accesorios_is_resolved(self):
        url = reverse('accesorios')
        self.assertEquals(resolve(url).func, accesorios)

    def test_prodAmplificador_is_resolved(self):
        url = reverse('prodAmplificador')
        self.assertEquals(resolve(url).func, prodAmplificador)

    def test_statusTrx_is_resolved(self):
        url = reverse('tbkRes')
        self.assertEquals(resolve(url).func, statusTrx)