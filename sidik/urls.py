from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('', RedirectView.as_view(url='device')),
    path('device/', include('apps.device.urls')),
    path('user/', include('apps.user.urls')),
    path('log/', include('apps.log.urls')),
]
