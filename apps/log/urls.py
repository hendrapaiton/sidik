from django.urls import path

from apps.log.views import log_index, log_message

urlpatterns = [
    path('', log_index, name='log-index'),
    path('message', log_message, name='log-message'),
]
