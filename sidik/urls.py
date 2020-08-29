from django.urls import path, include
from django.views.generic import RedirectView

from apps.log.views import log_index
from apps.login.views import login_index
from apps.user.views import user_index

urlpatterns = [
    path('', RedirectView.as_view(url='/device/')),
    path('device/', include('apps.device.urls')),
    path('user/', user_index, name='user-index'),
    path('login/', login_index, name='login-index'),
    path('log/', log_index, name='log-index'),
]
