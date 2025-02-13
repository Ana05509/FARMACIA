# Generated by Django 5.1.6 on 2025-02-13 02:49

import Farmacia.validador
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(max_length=255)),
                ('Telefono', models.CharField(blank=True, max_length=20, null=True)),
                ('Email', models.EmailField(blank=True, max_length=254, null=True, unique=True)),
                ('Direccion', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(max_length=255)),
                ('Telefono', models.CharField(blank=True, max_length=10, null=True, validators=[Farmacia.validador.validar_telefono])),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('Direccion', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Medicamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(max_length=255)),
                ('Descripcion', models.TextField(blank=True, null=True)),
                ('Precio', models.DecimalField(decimal_places=2, max_digits=10)),
                ('Stock', models.PositiveIntegerField()),
                ('Fecha_vencimiento', models.DateField()),
                ('Proveedor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Farmacia.proveedor')),
            ],
        ),
        migrations.CreateModel(
            name='Venta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Fecha_venta', models.DateTimeField(auto_now_add=True)),
                ('Total', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('Cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Farmacia.cliente')),
            ],
        ),
        migrations.CreateModel(
            name='DetalleVenta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.PositiveIntegerField()),
                ('precio_unitario', models.DecimalField(decimal_places=2, max_digits=10)),
                ('subtotal', models.DecimalField(decimal_places=2, editable=False, max_digits=10)),
                ('medicamento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Farmacia.medicamento')),
                ('venta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='detalles', to='Farmacia.venta')),
            ],
        ),
    ]
