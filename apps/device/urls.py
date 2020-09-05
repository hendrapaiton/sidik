from django.urls import path

from apps.device.views import create, read, update, delete, getac

urlpatterns = [
    path('create', create, name='device-create'),
    path('', read, name='device-read'),
    path('update/<int:id_device>', update, name='device-update'),
    path('delete/<int:id_device>', delete, name='device=delete'),
    path('getac', getac, name='getac'),
]
