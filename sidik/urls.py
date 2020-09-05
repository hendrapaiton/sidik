from django.urls import path, include
from django.views.generic import RedirectView

from apps.log.views import log_index

urlpatterns = [
    path('', RedirectView.as_view(url='device')),
    path('device/', include('apps.device.urls')),
    path('user/', include('apps.user.urls')),
    path('log/', log_index, name='log-index'),
]
