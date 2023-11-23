from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.core.cache import cache

from app.tasks import save_orders_clients
class GetSalesDataAPI(View):

    def get(self, request, *args, **kwargs):
        # Your data to be serialized as JSON
        data = cache.get('data')
        data = {'message': data, 'status': 'success'}

        # Create a JsonResponse object and return it
        return JsonResponse(data)


@method_decorator(csrf_exempt, name='dispatch')
class SaveOrdersAPI(View):

    def post(self, request, *args, **kwargs):
        orders = request.POST.get('orders', None)
        if orders is None:
            return JsonResponse({
                'message': "faltan ordenes",
                'status': 'failed'
            })
        save_orders_clients.delay(orders)

        # Create a JsonResponse object and return it
        return JsonResponse({
            'message': "guardado con exito",
            'status': 'success'
        })
