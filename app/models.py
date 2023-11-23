from django.db import models


class Canal(models.Model):
    nombre = models.CharField(max_length=120)


class Cliente(models.Model):
    ruc = models.CharField(max_length=120)
    nombrefactura = models.CharField(max_length=300)
    nombrefantasia = models.CharField(max_length=300)
    canalobj = models.ForeignKey(Canal, on_delete=models.CASCADE)


class Producto(models.Model):
    codigo = models.IntegerField()
    prod_marca = models.CharField(max_length=60)
    descripcion = models.CharField(max_length=120)


class Precios(models.Model):
    articuloobj = models.ForeignKey(Producto, on_delete=models.CASCADE)
    canalobj = models.ForeignKey(Canal, on_delete=models.CASCADE)
    precio = models.FloatField()
    fecha_vigencia = models.DateField()


class Orders(models.Model):
    pedido_numero = models.BigIntegerField(unique=True)
    pdvobj = models.ForeignKey(Cliente,
                               on_delete=models.SET_NULL,
                               null=True)
    doc_tipo = models.CharField(max_length=80)
    doc_fecha = models.DateField()
    doc_numero = models.BigIntegerField(default=0)
    anulado_040 = models.BooleanField(default=False)
    anulado_040_fecha = models.DateTimeField(null=True)
    anulado_040_por_gecos = models.CharField(max_length=120, null=True)


class OrdersDetail(models.Model):
    orderobj = models.ForeignKey(Orders, on_delete=models.CASCADE)
    artobj = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad_original = models.IntegerField()
    cantidad = models.IntegerField()
    precio_unitario = models.FloatField()
    iva_10 = models.FloatField()
    gravada_10 = models.FloatField()
    iva_5 = models.FloatField()
    gravada_5 = models.FloatField()
    exenta = models.FloatField()
    anulado_040 = models.BooleanField(default=False)
    anulado_040_fecha = models.DateTimeField(null=True)
    anulado_040_por_gecos = models.CharField(max_length=120, null=True)
