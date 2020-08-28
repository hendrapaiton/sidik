from django.urls import path
from django.views.generic import RedirectView

from apps.device.views import device_index
from apps.log.views import log_index
from apps.login.views import login_index
from apps.user.views import user_index

urlpatterns = [
    path('', RedirectView.as_view(url='/device/')),
    path('device/', device_index, name='device-index'),
    path('user/', user_index, name='user-index'),
    path('login/', login_index, name='login-index'),
    path('log/', log_index, name='log-index'),
]
