from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from app import views

app_name = 'app'

urlpatterns = [
    path('download/', views.DownloadData.as_view(), name='download_data'),
    path('upload/', views.UploadOrdersView.as_view(), name='upload_data'),
    path('api/v1/get-sales-data/', views.GetSalesDataAPI.as_view(), name='get_sales_data_api'),
    path('api/v1/save-orders/', views.SaveOrdersAPI.as_view(), name='save_orders_api'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
