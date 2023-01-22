# Generated by Django 3.2.16 on 2023-01-21 23:33

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='cargo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
                ('descripcio', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200, null=True)),
                ('email', models.CharField(max_length=200, null=True)),
                ('usuario', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='contacto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('correo', models.EmailField(max_length=254)),
                ('tipo_consulta', models.IntegerField(choices=[[0, 'Consulta'], [1, 'Reclamo'], [2, 'Sugerencia'], [3, 'Felicitaciones'], [4, 'Solicitud de Proveedor']])),
                ('mensaje', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='familia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.categoria')),
            ],
        ),
        migrations.CreateModel(
            name='orden',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('orden_fecha', models.DateTimeField(auto_now_add=True)),
                ('complete', models.BooleanField(default=False)),
                ('transaccion_id', models.CharField(max_length=100, null=True)),
                ('cliente', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.cliente')),
            ],
        ),
        migrations.CreateModel(
            name='proveedor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rut', models.IntegerField()),
                ('nombre', models.TextField()),
                ('telefono', models.IntegerField()),
                ('rubro', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('descripcion', models.TextField(max_length=300)),
                ('precio', models.IntegerField()),
                ('vencimiento', models.DateField()),
                ('stock', models.IntegerField()),
                ('stock_critico', models.IntegerField()),
                ('imagen', models.ImageField(null=True, upload_to='productos')),
                ('oferta', models.BooleanField(default='0')),
                ('familia', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.familia')),
                ('proveedor', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.proveedor')),
            ],
        ),
        migrations.CreateModel(
            name='persona',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rut', models.IntegerField()),
                ('nombre', models.TextField()),
                ('telefono', models.IntegerField()),
                ('User', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('cargo', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.cargo')),
            ],
        ),
        migrations.CreateModel(
            name='ordenItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField(blank=True, default=0, null=True)),
                ('fecha_agregada', models.DateTimeField(auto_now_add=True)),
                ('orden', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.orden')),
                ('producto', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.producto')),
            ],
        ),
        migrations.CreateModel(
            name='factura',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField(default=datetime.datetime.today)),
                ('canitdad_producto', models.IntegerField()),
                ('total', models.IntegerField()),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.producto')),
            ],
        ),
        migrations.CreateModel(
            name='direccion_envio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('direccion', models.CharField(max_length=200)),
                ('ciudad', models.CharField(max_length=200)),
                ('Region', models.CharField(max_length=200)),
                ('codigo_postal', models.CharField(max_length=200)),
                ('fecha_agregada', models.DateTimeField(auto_now_add=True)),
                ('cliente', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.cliente')),
                ('orden', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.orden')),
            ],
        ),
        migrations.CreateModel(
            name='boleta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField(default=datetime.datetime.today)),
                ('canitdad_producto', models.IntegerField()),
                ('total', models.IntegerField()),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.producto')),
            ],
        ),
    ]