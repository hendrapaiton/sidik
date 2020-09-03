from django.urls import path

from apps.user.views import read, create, update, delete

urlpatterns = [
    path('create/', create, name='user-create'),
    path('', read, name='user-read'),
    path('update/<int:id_user>/', update, name='user-update'),
    path('delete/<int:id_user>', delete, name='user-delete'),
]
