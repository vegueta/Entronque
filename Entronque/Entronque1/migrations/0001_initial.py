# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='almacen',
            fields=[
                ('idproducto', models.IntegerField(serialize=False, primary_key=True)),
                ('cantidad', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='bebidas',
            fields=[
                ('idbebida', models.IntegerField(serialize=False, primary_key=True)),
                ('nombre', models.CharField(max_length=30)),
                ('presentacion', models.CharField(max_length=30)),
                ('sabor', models.CharField(max_length=15)),
                ('idproducto', models.ForeignKey(to='Entronque1.almacen')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='compras',
            fields=[
                ('idcompra', models.IntegerField(serialize=False, primary_key=True)),
                ('producto', models.CharField(max_length=30)),
                ('costo', models.FloatField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='personal',
            fields=[
                ('idpersona', models.IntegerField(serialize=False, primary_key=True)),
                ('nombre', models.CharField(max_length=30)),
                ('apellido', models.CharField(max_length=30)),
                ('direccion', models.CharField(max_length=50)),
                ('telefono', models.IntegerField()),
                ('email', models.CharField(max_length=30)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='platillos',
            fields=[
                ('idplatillo', models.IntegerField(serialize=False, primary_key=True)),
                ('nombre', models.CharField(max_length=20)),
                ('tipo', models.CharField(max_length=20)),
                ('costo', models.FloatField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='proveedores',
            fields=[
                ('idproveedor', models.IntegerField(serialize=False, primary_key=True)),
                ('nombre', models.CharField(max_length=30)),
                ('direccion', models.CharField(max_length=50)),
                ('telefono', models.IntegerField()),
                ('email', models.CharField(max_length=30)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ventasbebidas',
            fields=[
                ('idventa_b', models.IntegerField(serialize=False, primary_key=True)),
                ('producto', models.CharField(max_length=30)),
                ('total', models.IntegerField()),
                ('idbebida', models.ForeignKey(to='Entronque1.bebidas')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ventasplatillo',
            fields=[
                ('idventa_p', models.IntegerField(serialize=False, primary_key=True)),
                ('producto', models.CharField(max_length=20)),
                ('total', models.IntegerField()),
                ('idplatillo', models.ForeignKey(to='Entronque1.platillos')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='compras',
            name='idproveedor',
            field=models.ForeignKey(to='Entronque1.proveedores'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='almacen',
            name='idcompra',
            field=models.ForeignKey(to='Entronque1.compras'),
            preserve_default=True,
        ),
    ]
