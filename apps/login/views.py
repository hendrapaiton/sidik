from django.shortcuts import render


def login_index(request):
    context = {
        'menu': 'login'
    }
    return render(request, 'apps/login/index.html', context)
