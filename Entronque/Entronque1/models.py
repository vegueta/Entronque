from django.db import models

class personal(models.Model):
    idpersona=models.IntegerField(primary_key=True)
    nombre= models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    direccion=models.CharField(max_length=50)
    telefono =models.IntegerField()
    email= models.CharField(max_length=30)

class proveedores(models.Model):
    idproveedor=models.IntegerField(primary_key=True)
    nombre= models.CharField(max_length=30)
    direccion=models.CharField(max_length=50)
    telefono =models.IntegerField()
    email= models.CharField(max_length=30)

class platillos(models.Model):
    idplatillo=models.AutoField(primary_key=True)
    nombre= models.CharField(max_length=20)
    tipo = models.CharField(max_length=20)
    costo= models.FloatField()

class ventasplatillo(models.Model):
    idventa_p=models.AutoField(primary_key=True)
    idplatillo= models.ForeignKey(platillos)
    producto=models.CharField(max_length=20)
    total=models.IntegerField()

class compras(models.Model):
    idcompra=models.AutoField(primary_key=True)
    idproveedor= models.ForeignKey(proveedores,on_delete=models.CASCADE,)
    producto= models.CharField(max_length=30)
    costo= models.FloatField()

class almacen(models.Model):
    idproducto=models.AutoField(primary_key=True)
    cantidad=models.IntegerField()
    idcompra= models.ForeignKey(compras)

class bebidas(models.Model):
    idbebida=models.AutoField(primary_key=True)
    idproducto= models.ForeignKey(almacen)
    nombre= models.CharField(max_length=30)
    presentacion= models.CharField(max_length=30)
    sabor= models.CharField(max_length=15)


class ventasbebidas(models.Model):
    idventa_b=models.AutoField(primary_key=True)
    idbebida= models.ForeignKey(bebidas)
    producto=models.CharField(max_length=30)
    total=models.IntegerField()
    
    
