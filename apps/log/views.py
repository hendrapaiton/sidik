from django.shortcuts import render


def log_index(request):
    context = {
        'menu': 'log'
    }
    return render(request, 'apps/log/index.html', context)
