import json
import lzstring
from datetime import datetime
from django.core.cache import cache
from django.db import transaction

from celery import shared_task

from app.models import Orders, OrdersDetail

compressor = lzstring.LZString()

@shared_task
def save_orders_clients(compressedOrdersData):

    # En el BE descomprimir los datos con lzstring.
    orders_json = compressor.decompressFromUTF16(compressedOrdersData)
    # Convertir el JSON a tipo de datos python.
    client_orders = json.loads(orders_json)
    ultimo_pedido = Orders.objects.last()
    numero_pedido = 0
    if ultimo_pedido is not None:
        numero_pedido = ultimo_pedido.pedido_numero

    # Guardos los datos en la base de datos.
    with transaction.atomic():
        for client_id, client_order_items in client_orders.items():
            numero_pedido += 1
            order = Orders(pedido_numero=numero_pedido,
                           pdvobj_id=client_id,
                           doc_tipo="doct_tipo",
                           doc_fecha=datetime.now().date())
            order.save()
            for client_order in client_order_items:
                order_detail = OrdersDetail(**client_order)
                order_detail.orderobj = order
                order_detail.save()


@shared_task
def save_sales_data(data: dict):
    # Comprimir el json con lzstring.
    compressor = lzstring.LZString()

    # Convertir a json la estructura.
    data_json = json.dumps(data)

    # Guarda la estructura comprimida en la base de datos redis
    compressed = compressor.compressToUTF16(data_json)
    # Guarda en Redis
    cache.set("data", compressed)
