from django.shortcuts import render


def device_index(request):
    context = {
        'menu': 'device'
    }
    return render(request, 'apps/device/index.html', context)
