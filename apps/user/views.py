from django.shortcuts import render


def user_index(request):
    context = {
        'menu': 'user'
    }
    return render(request, 'apps/user/index.html', context)
