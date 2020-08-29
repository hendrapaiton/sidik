from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render

from apps.device.forms import DeviceForm
from apps.device.models import Device


def device(request, function='read'):
    devices = Device.objects.all()
    form = DeviceForm(request.POST or None)
    if request.method == 'GET' and function == 'create':
        context = {
            'form': form,
            'menu': 'device'
        }
        return render(request, 'apps/device/create.html', context)
    elif request.method == 'GET' and function == 'read':
        context = {
            'devices': devices,
            'menu': 'device',
        }
        return render(request, 'apps/device/index.html', context)
    elif request.method == 'GET' and function == 'delete':
        pass
    elif request.method == 'POST' and function == 'create':
        form = DeviceForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reversed('device'))
        else:
            form = DeviceForm()
            context = {
                'form': form,
                'menu': 'device'
            }
            return render(request, 'apps/device/create.html', context)
    else:
        raise Http404('Denied by request filtering configuration')
