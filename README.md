
### CARGA PEDIDOS ####

Crear un proyecto Django + Celery + Redis. El proyecto debe hacer lo siguiente.


* Crear un metodo llamado save_sales_data

   (tiene que ser un metodo dentro de la estructura Django y debe tener la posibilidad de ser ejecutado como una tarea celery )

* Crear una estructura de datos diccionario con la informacion necesaria para la venta.

    Eje:
     ```
       gart = {'clientes': {[cliente_id]: {'nombrefantasia': 'beto' ... } 
                              ....
                              },
                 'articulos': {[articulo_id]: {...[datos por llaves del articulo] ... }
                               ...
                              }
                 ...
       }
     ```

* Convertir a json la estructura.    

* Comprimir el json con lzstring.

* Guarda la estructura comprimida en la base de datos redis.

* Crear un endpoint para retraer los datos guardados en redis desde el cliente navegador.

* Guardar los datos comprimidos en localstorage.

* A medida que se retrae los datos del localstorage con getItem, descomprimir los datos.

* Crear una estructura de objecto javascript que contenga los datos de carga de un pedido (Modelo Orders).

    Eje: 
     ```
      orders = {  
        [cliente_id_uno]: [
            { [articulo_id], [precio_unitario], [gravada_10], [iva_10], ... }
        ],
        [cliente_id_dos]: [
            { [articulo_id], [precio_unitario], [gravada_10], [iva_10], ... }
        ],
        [cliente_id_tres]: [
            { [articulo_id], [precio_unitario], [gravada_10], [iva_10], ... }
        ]
        ...
      }
     ```

* Convertir este objecto a JSON.

* Comprimir el JSON con lzstring.

* Guardar en el localstorage.

* Traer los datos del orders guardado con getItem.

* Enviarlo a un endpoint en el BE.

* Este endpoint debe llamar al metodo save_orders_clients

  (save_orders_clients debe ser llamado como una tarea celery )

  Esto por que las Orders pueden ser muy grandes y el cliente no debe de esperar el procesamiento de toda la Order, sino pasarlo al proceso de Celery.

* Ya dentro de save_orders_clients, el mismo debe de 

  * En el BE descomprimir los datos con lzstring.

  * convertir el JSON a tipo de datos python.

  * Guardos los datos en la base de datos.



BONUS: Si integras Django con Sentry, son puntos extras.


#### Estructura de Modelos

```
from django.db import models

class Canal(models.Model):
    nombre = models.CharField(max_length=120)

class Cliente(models.Model):
    ruc = models.CharField(max_length=120)
    nombrefactura = models.CharField(max_length=300)
    nombrefantasia = models.CharField(max_length=300)
    canalobj = models.ForeignKey('Canal')


class Producto(models.Model):
    codigo = models.IntegerField()
    prod_marca = models.CharField(max_length=60)
    descripcion = models.CharField(max_length=120)


class Precios(models.Model):
    articuloobj = models.ForeignKey('Producto')
    canalobj = models.ForeignKey('Canal')
    precio = models.FloatField()
    fecha_vigencia = models.DateField()

class Orders(models.Model):
    pedido_numero = models.BigIntegerField(unique=True)
    pdvobj = models.ForeignKey(Cliente)
    doc_tipo = models.CharField(max_length=80)
    doc_fecha = models.DateField()
    doc_numero = models.BigIntegerField(default=0)
    anulado_040 = models.BooleandField(default=False)
    anulado_040_fecha = models.DateTimeField(null=True)
    anulado_040_por_gecos = models.CharField(null=True)

class OrdersDetail(models.Model):
    orderobj = models.ForeignKey(Orders)
    artobj = models.ForeignKey(Producto)
    cantidad_original = models.IntegerField()
    cantidad = models.IntegerField()
    precio_unitario = models.FloatField()
    iva_10 = models.FloatField()
    gravada_10 = models.FloatField()
    iva_5 = models.FloatField()
    gravada_5 = models.FloatField()
    exenta = models.FloatField()
    anulado_040 = models.BooleandField(default=False)
    anulado_040_fecha = models.DateTimeField(null=True)
    anulado_040_por_gecos = models.CharField(null=True)
```
