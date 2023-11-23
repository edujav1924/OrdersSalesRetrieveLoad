from django.views.generic import TemplateView

from app.tasks import  save_sales_data


class DownloadData(TemplateView):
    template_name = 'download_data.html'

    def get(self, request, *args, **kwargs):
        sales_data = {
            'clientes': {
                100: {
                    'nombrefantasia': 'Empresa_1 SA',
                    'nombrefactura': 'empresa_1',
                    'canalID': 1,
                    'ruc': '5552003-0'
                },
                101: {
                    'nombrefantasia': 'Empresa_2 SA',
                    'nombrefactura': 'empresa_2',
                    'canalID': 2,
                    'ruc': '5552005-0'
                },
                102: {
                    'nombrefantasia': 'Empresa_3 SA',
                    'nombrefactura': 'empresa_3',
                    'canalID': 3,
                    'ruc': '5552004-0'
                }
            },
            'articulos': {
                9000: {
                    'descripcion': 'Laptop',
                    'precio': 1200,
                    'stock': 50
                },
                9001: {
                    'descripcion': 'Teléfono',
                    'precio': 500,
                    'stock': 100
                },
                9002: {
                    'descripcion': 'Radio',
                    'precio': 100,
                    'stock': 20
                },
            }
        }
        save_sales_data.delay(sales_data)
        return super().get(request, *args, **kwargs)


class UploadOrdersView(TemplateView):

    template_name = 'upload_data.html'
