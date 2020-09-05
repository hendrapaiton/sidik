from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render


def log_index(request):
    context = {
        'menu': 'log'
    }
    return render(request, 'apps/log/index.html', context)


def log_message(request):
    user_name = request.GET.get('user_name')
    time = request.GET.get('time')
    if user_name is not None and time is not None:
        return HttpResponse(user_name + ' login success on ' + str(datetime.strptime(time, '%Y%m%d%H%M%S')))
    else:
        message = request.GET.get('msg')
        return HttpResponse(message)
