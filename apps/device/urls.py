from django.urls import path

from apps.device.views import device

urlpatterns = [
    path('', device, name='device'),
    path('<str:function>/', device, name='device'),
]
