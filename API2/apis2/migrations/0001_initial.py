# Generated by Django 3.2.16 on 2023-01-21 23:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='proveedor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rut', models.IntegerField()),
                ('nombre', models.TextField()),
                ('telefono', models.IntegerField()),
                ('rubro', models.TextField()),
            ],
            options={
                'db_table': 'core_proveedor',
                'managed': False,
            },
        ),
    ]
