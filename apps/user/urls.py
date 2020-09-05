from django.urls import path

from apps.user.views import read, create, update, delete, user_register, process_register, user_verification, process_verification

urlpatterns = [
    path('create', create, name='user-create'),
    path('', read, name='user-read'),
    path('update/<int:id_user>', update, name='user-update'),
    path('delete/<int:id_user>', delete, name='user-delete'),
    path('register', user_register, name='user-register'),
    path('register/process', process_register, name='process-register'),
    path('verification', user_verification, name='user-verification'),
    path('verification/process', process_verification, name='process-verification')
]
